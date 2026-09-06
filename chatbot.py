"""Conversation engine for the Rural Health Chatbot.

Two supported flows:

1. Symptom -> diagnosis
   User types symptoms. The bot matches diseases, then asks one clarifying
   yes/no question at a time to narrow down, and finally gives the most
   likely disease with medicines, precautions, diet and doctor advice.

2. Disease -> guidance
   User types a disease name. The bot confirms by asking a few symptom
   questions and then gives management suggestions for that disease.

Every medical answer carries a disclaimer. This tool is an educational aid,
not an actual doctor.
"""

import re

from diseases import DISEASES, DISEASE_ALIASES, SYMPTOM_ALIASES

GREETING = [
    "Namaste! I am your Rural Health Chatbot. I am here to help you understand"
    " common health problems at home.",
    "You can do two things with me:",
    "1. Tell me your SYMPTOMS and I will ask a few questions and suggest the"
    " most likely disease and home care.",
    "2. Tell me a DISEASE NAME (for example malaria, cold, sugar, acidity) and"
    " I will ask some questions and give its suggestions.",
    "I am not a doctor and cannot replace one. For serious problems, always go"
    " to your health centre or doctor.",
]

HELP_TEXT = (
    "I did not understand that fully. Try telling me symptoms like:\n"
    "- \"I have fever and headache\"\n"
    "- \"cough since many weeks\"\n"
    "- \"burning while urinating\"\n"
    "Or tell me a disease name like: malaria, cold, flu, typhoid, dengue, "
    "acidity, sugar, blood pressure, TB, ringworm, pink eye, UTI."
)

AFTER_DIAGNOSIS = (
    "You can ask me about another symptom or disease anytime. For example:\n"
    "- \"I have stomach pain and vomiting\"\n"
    "- \"tell me about diabetes\""
)

DISCLAIMER = (
    "IMPORTANT: This is general home-care information for rural health, not a"
    " medical prescription. Always check with a doctor or health worker before"
    " taking any medicine. If symptoms are serious or last long, visit your"
    " nearest health centre."
)


def normalize(text):
    return re.sub(r"[^a-z0-9\s']", " ", text.lower())


def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def contains_phrase(alias, message):
    """True if the alias phrase appears in the message as whole words."""
    words = re.findall(r"[a-z0-9']+", alias.lower())
    if not words:
        return False
    return all(w in tokenize(message) for w in words)


def detect_disease(message):
    """Return disease key if the message clearly names a disease, else None."""
    toks = tokenize(message)
    for key, aliases in DISEASE_ALIASES.items():
        for alias in aliases:
            words = re.findall(r"[a-z0-9']+", alias.lower())
            if words and all(w in toks for w in words):
                return key
    return None


def detect_symptoms(message):
    """Return the set of canonical symptom phrases found in the message."""
    found = []
    msg = " " + normalize(message) + " "
    for alias, canonical in SYMPTOM_ALIASES.items():
        if contains_phrase(alias, msg):
            if canonical not in found:
                found.append(canonical)
    return found


def parse_yes_no(message):
    toks = tokenize(message)
    yes_words = {"yes", "ya", "y", "yeah", "yep", "sure", "maybe", "may be",
                 "probably", "likely", "sometimes", "a little", "little",
                 "slightly", "somewhat", "definitely", "true"}
    no_words = {"no", "nah", "n", "nope", "not", "never", "noo", "not at all"}
    if toks & yes_words and not (toks & no_words):
        return True
    if toks & no_words:
        return False
    return None


def question_text(disease_key, symptom):
    return f"Do you have {symptom}?"


class HealthChatbot:
    MAX_CLARIFY_QUESTIONS = 4
    MIN_SCORE = 4
    MIN_GAP = 1
    NO_PENALTY = 0.8  # how much a denied strong symptom cuts a score

    def __init__(self, diseases=DISEASES):
        self.diseases = diseases

    # ----- state helpers ---------------------------------------------------
    def _start_state(self):
        return {
            "phase": "new",          # new | clarify | disease_confirm
            "matched": [],           # canonical symptoms found/confirmed
            "absent": [],            # canonical symptoms the user denied
            "candidates": [],        # candidate disease keys
            "asked": [],             # symptom phrases already asked
            "asked_count": 0,
            "disease_key": None,     # for disease_confirm flow
            "confirm_yes": 0,
            "q": [],                 # remaining questions (disease flow)
            "q_index": 0,
        }

    def _matched(self, state):
        return set(state["matched"])

    def _absent(self, state):
        return set(state["absent"])

    def score(self, key, matched, absent=()):
        score = 0.0
        for sym, w in self.diseases[key]["symptoms"]:
            if sym in matched:
                score += w
        for sym, w in self.diseases[key]["symptoms"]:
            if w >= 2 and sym in absent:
                score -= w * self.NO_PENALTY
        return max(0.0, score)

    # ----- reply helpers ----------------------------------------------------
    def greeting(self):
        return [{"kind": "text", "text": t} for t in GREETING]

    def text(self, t):
        return {"kind": "text", "text": t}

    # ----- flow: symptom diagnosis ------------------------------------------
    def _start_diagnosis(self, state, symptoms):
        matched = set(symptoms)
        ranked = [
            (key, self.score(key, matched))
            for key in self.diseases
            if self.score(key, matched) > 0
        ]
        ranked.sort(key=lambda x: x[1], reverse=True)
        state["phase"] = "clarify"
        state["matched"] = list(matched)
        state["candidates"] = [k for k, _ in ranked]
        state["asked"] = []

    def _next_question(self, state):
        """Pick the best next yes/no question, or None if done."""
        ranked = sorted(
            state["candidates"],
            key=lambda k: self.score(k, self._matched(state),
                                     self._absent(state)),
            reverse=True,
        )
        asked = set(state["asked"])
        matched = self._matched(state)
        for key in ranked:
            syms = sorted(self.diseases[key]["symptoms"],
                          key=lambda x: x[1], reverse=True)
            for sym, _ in syms:
                if sym not in matched and sym not in asked:
                    state["asked"].append(sym)
                    state["asked_count"] += 1
                    return key, sym
        return None

    def _decide(self, state):
        matched, absent = self._matched(state), self._absent(state)
        ranked = sorted(
            state["candidates"],
            key=lambda k: self.score(k, matched, absent),
            reverse=True,
        )
        if not ranked:
            return None
        top = ranked[0]
        top_score = self.score(top, matched, absent)
        second_score = (self.score(ranked[1], matched, absent)
                        if len(ranked) > 1 else 0)
        if top_score >= self.MIN_SCORE and (top_score - second_score) >= self.MIN_GAP:
            return {"key": top, "confident": True}
        return {"key": top, "confident": False}

    def _diagnosis_reply(self, state, decision):
        state["phase"] = "new"
        key = decision["key"]
        d = self.diseases[key]
        matched = ", ".join(state["matched"]) or "your answers"
        lines = []
        if decision["confident"]:
            lines.append(
                "Based on what you told me, the most likely problem is: "
                f"{d['name']}.")
        else:
            lines.append(
                f"Your symptoms point most towards {d['name']}, but I cannot"
                " be fully sure. Please get a proper check-up at the health"
                " centre.")
        lines.append("")
        lines.append(f"Symptoms you reported: {matched}.")
        self._append_guidance(lines, d)
        lines.append("")
        lines.append(DISCLAIMER)
        lines.append("")
        lines.append(AFTER_DIAGNOSIS)
        return [self.text("\n".join(lines))]

    # ----- flow: disease guidance --------------------------------------------
    def _start_disease_confirm(self, state, key):
        state["phase"] = "disease_confirm"
        state["disease_key"] = key
        state["q"] = [sym for sym, w in self.diseases[key]["symptoms"]
                      if w >= 2]
        state["q_index"] = 0
        state["confirm_yes"] = 0

    def _guidance_reply(self, state, prompted=False):
        key = state["disease_key"]
        d = self.diseases[key]
        state["phase"] = "new"
        lines = []
        if prompted and state["q"]:
            yes = state["confirm_yes"]
            if yes == 0:
                lines.append(
                    "Since you do not seem to have the main symptoms of "
                    f"{d['name']}, you might be describing something else. "
                    "Please describe your exact symptoms, or see your doctor.")
            else:
                lines.append(
                    f"You have {yes} of the common symptoms of {d['name']}."
                    " Here is the guidance for it:")
        else:
            lines.append(f"Here is the guidance for {d['name']}.")
        self._append_guidance(lines, d)
        lines.append("")
        lines.append(DISCLAIMER)
        lines.append("")
        lines.append(AFTER_DIAGNOSIS)
        return [self.text("\n".join(lines))]

    def _append_guidance(self, lines, d):
        meds = d.get("medicines") or []
        if meds:
            lines.append("")
            lines.append("Suggested medicines / first aid:")
            for m in meds:
                lines.append("- " + m)
        else:
            lines.append("")
            lines.append("Suggested medicines / first aid: this should only"
                         " be handled by a doctor — no home treatment here.")
        lines.append("")
        lines.append("Precautions:")
        for p in d.get("precautions") or ["Follow the doctor's advice."]:
            lines.append("- " + p)
        lines.append("")
        lines.append("Food and rest (Diet):")
        for di in d.get("diet") or ["Eat a normal, nutritious diet."]:
            lines.append("- " + di)
        lines.append("")
        lines.append("See a doctor immediately if:")
        for wk in d.get("when_doctor") or []:
            lines.append("- " + wk)

    # ----- main entry ---------------------------------------------------------
    def handle(self, state, message):
        if not isinstance(state, dict) or "phase" not in state:
            state = self._start_state()

        msg = (message or "").strip()
        low = msg.lower()

        if not msg:
            return ([self.text(HELP_TEXT)], state)

        if low in ("help", "what can you do", "how do i use this"):
            return ([self.text(HELP_TEXT)], state)

        phase = state.get("phase")

        # ---- disease confirm flow: process yes/no answers -------------------
        if phase == "disease_confirm":
            key = state.get("disease_key")
            q = state["q"]
            idx = state["q_index"]
            answer = parse_yes_no(msg)
            if answer is True:
                state["confirm_yes"] += 1
            elif answer is not False and detect_symptoms(msg):
                state["confirm_yes"] += 1
            idx += 1
            state["q_index"] = idx
            if idx < len(q) and idx < 4:
                return ([self.text(question_text(key, q[idx]))], state)
            return (self._guidance_reply(state, prompted=True), state)

        # ---- clarify flow: process yes/no answers ---------------------------
        if phase == "clarify":
            # allow switching to a disease name mid-flow
            disease_key = detect_disease(msg)
            if disease_key:
                d = self.diseases[disease_key]
                self._start_disease_confirm(state, disease_key)
                q = state["q"]
                replies = [
                    self.text(f"You asked about {d['name']}. Let me ask you a"
                              " few quick questions to give the right"
                              " suggestions.")
                ]
                replies.append(self.text(question_text(
                    disease_key, q[0])) if q else
                    self._guidance_reply(state, prompted=False)[0])
                return (replies, state)

            answer = parse_yes_no(msg)
            if answer is None:
                new_syms = detect_symptoms(msg)
                if new_syms:
                    for s in new_syms:
                        if s not in state["matched"]:
                            state["matched"].append(s)
                    next_q = self._next_question(state)
                    if next_q is None:
                        return (self._diagnosis_reply(state,
                                                      self._decide(state)),
                                state)
                    _, sym = next_q
                    return ([self.text(question_text(next_q[0], sym))], state)
                return ([self.text("Please answer yes or no.")], state)

            asked_sym = state["asked"][-1] if state["asked"] else None
            if answer is True and asked_sym:
                if asked_sym not in state["matched"]:
                    state["matched"].append(asked_sym)
            elif answer is False and asked_sym:
                if asked_sym not in state["absent"]:
                    state["absent"].append(asked_sym)
                matched, absent = self._matched(state), self._absent(state)
                pruned = [
                    k for k in state["candidates"]
                    if self.score(k, matched, absent) > 0
                ]
                if not pruned:
                    pruned = state["candidates"]
                state["candidates"] = pruned

            next_q = self._next_question(state)
            decision = self._decide(state)
            if (next_q is None
                    or state["asked_count"] >= self.MAX_CLARIFY_QUESTIONS
                    or decision["confident"]):
                return (self._diagnosis_reply(state, decision), state)
            _, sym = next_q
            return ([self.text(question_text(next_q[0], sym))], state)

        # ---- new message: decide intent -------------------------------------
        if parse_yes_no(msg) is not None:
            return ([self.text(AFTER_DIAGNOSIS)], state)

        disease_key = detect_disease(msg)
        if disease_key:
            d = self.diseases[disease_key]
            replies = [
                self.text(f"You asked about {d['name']}. Let me ask you a few"
                          " quick questions to give the right suggestions.")
            ]
            self._start_disease_confirm(state, disease_key)
            q = state["q"]
            if q:
                replies.append(self.text(question_text(disease_key, q[0])))
            else:
                replies += self._guidance_reply(state, prompted=False)
            return (replies, state)

        symptoms = detect_symptoms(msg)
        if symptoms:
            self._start_diagnosis(state, symptoms)
            s = ", ".join(symptoms)
            next_q = self._next_question(state)
            replies = [
                self.text(f"I noted these symptoms: {s}. Let me ask a couple"
                          " of questions to narrow it down.")
            ]
            if next_q is None:
                replies += self._diagnosis_reply(state, self._decide(state))
            else:
                _, sym = next_q
                replies.append(self.text(question_text(next_q[0], sym)))
            return (replies, state)

        return ([self.text(HELP_TEXT)], state)