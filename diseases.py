"""Sample disease knowledge base for the Rural Health Chatbot.

Each disease entry has:
- name        : display name of the disease
- symptoms    : list of (canonical symptom phrase, weight). Weight 2 = strong
                sign of the disease, weight 1 = common/less specific sign.
- medicines   : symptom relief / first-aid suggestions (NOT prescriptions)
- precautions : things to do / avoid
- diet        : food and rest advice
- when_doctor : signs that mean the person must see a doctor or go to hospital

This is SAMPLE educational data. Real trust tables / clinical protocols should
replace it for production use, and every answer carries a disclaimer.
"""

DISEASES = {
    "common_cold": {
        "name": "Common Cold",
        "symptoms": [
            ("runny or stuffy nose", 2),
            ("sneezing", 1),
            ("sore throat", 2),
            ("cough", 1),
            ("mild fever", 1),
            ("headache", 1),
        ],
        "medicines": [
            "Paracetamol for fever or body ache (250-500 mg, up to 4 times a day, with food) — only for temporary relief",
            "Saline nasal drops or steam inhalation to open a blocked nose",
            "Warm salt-water gargle and warm honey-ginger tea for the sore throat",
            "Take rest, keep warm, and drink plenty of warm fluids",
        ],
        "precautions": [
            "Avoid touching others' faces and wash hands often to avoid spreading it",
            "Avoid cold water, cold drinks and chill drafts",
            "Do not take antibiotics — a cold is caused by a virus, antibiotics will not help",
            "Do not give aspirin to children below 12 years",
        ],
        "diet": [
            "Take light, warm food: dal-rice, khichdi, vegetable soup",
            "Drink lots of fluids: warm water, lemon-honey water, herbal tea",
        ],
        "when_doctor": [
            "Fever lasts more than 3-4 days or body temperature stays very high",
            "Difficulty in breathing or chest pain develops",
            "Symptoms last more than 10 days or get worse",
            "The sick person is a child below 3 years, an elderly person, or a pregnant woman",
        ],
    },

    "influenza": {
        "name": "Influenza (Seasonal Flu)",
        "symptoms": [
            ("high fever", 2),
            ("body ache", 2),
            ("headache", 2),
            ("cough", 2),
            ("fatigue", 2),
            ("chills", 2),
            ("sore throat", 1),
        ],
        "medicines": [
            "Paracetamol (500 mg) every 6-8 hours for fever and body ache — temporary relief only",
            "Rest in bed, keep the room airy and warm",
            "Plenty of fluids, ORS or lime water to prevent dehydration",
            "Salt-water gargle for the throat",
        ],
        "precautions": [
            "Avoid aspirin in children under 12 years (risk of Reye's syndrome)",
            "Do not stop drinking water even if throat hurts",
            "Stay away from others while fever lasts; cover face while coughing or sneezing",
            "Do not take antibiotics unless a doctor prescribes them",
        ],
        "diet": [
            "Warm soup, khichdi, boiled vegetables, soft fruits",
            "Drink warm water every 1-2 hours",
        ],
        "when_doctor": [
            "Fever above 39-40 C or lasting more than 3 days",
            "Difficulty breathing, chest pain, confusion or fits",
            "Child, elderly person, pregnant woman, or someone with diabetes/BP gets the flu",
            "Symptoms seem to improve and then come back worse",
        ],
    },

    "viral_fever": {
        "name": "Viral Fever (General)",
        "symptoms": [
            ("high fever", 2),
            ("body ache", 2),
            ("headache", 2),
            ("fatigue", 2),
            ("nausea", 1),
            ("chills", 1),
            ("loss of appetite", 1),
        ],
        "medicines": [
            "Paracetamol (500 mg) every 6-8 hours for fever and aches — do not exceed 4 doses a day",
            "Sponge the body with a wet cloth if fever is very high",
            "Plenty of fluids and complete rest",
        ],
        "precautions": [
            "Do not take antibiotics on your own — they do not work on viruses",
            "Do not take two fever medicines together (paracetamol + other brand that also contains paracetamol)",
            "Rest until fever is completely gone for at least 24 hours",
        ],
        "diet": [
            "Light, easy-to-digest food: idli, khichdi, dal rice, soup",
            "Drink a glass of water or ORS every 1-2 hours",
        ],
        "when_doctor": [
            "Fever lasts more than 3 days or is very high (above 40 C)",
            "Stiff neck, severe headache, confusion, vomiting that does not stop, or skin colour changes",
            "Very young or old patient, or a pregnant woman",
            "Fever comes with rash, difficulty in breathing, or pain in chest",
        ],
    },

    "malaria": {
        "name": "Malaria",
        "symptoms": [
            ("fever with chills", 3),
            ("high fever", 2),
            ("headache", 2),
            ("sweating after fever", 2),
            ("fatigue", 2),
            ("vomiting", 1),
            ("nausea", 1),
            ("body ache", 1),
        ],
        "medicines": [
            "Paracetamol (500 mg) for fever as temporary relief only",
            "Anti-malarial medicine MUST be taken only after a blood test confirms malaria and a doctor chooses the drug",
            "Drink plenty of fluids and ORS to replace what is lost",
        ],
        "precautions": [
            "Do NOT take malaria medicines on your own — wrong dose is dangerous and can fail",
            "Use a mosquito net, especially at night, and remove stagnant water around the house",
            "Keep the patient covered and at rest once fever starts",
        ],
        "diet": [
            "Light meals like khichdi, porridge, fruit",
            "Plenty of water, ORS, coconut water",
        ],
        "when_doctor": [
            "Get a blood smear / RDT test done at a health centre if fever comes with chills and sweating cycles",
            "Fever with vomiting that does not stop, fits, drowsiness, or yellow eyes — go to hospital immediately",
            "Pregnant women or small children with fever must be checked the same day",
        ],
    },

    "dengue": {
        "name": "Dengue Fever",
        "symptoms": [
            ("high fever", 3),
            ("severe headache behind eyes", 2),
            ("body ache", 2),
            ("joint pain", 2),
            ("skin rash", 2),
            ("nausea", 1),
            ("bleeding gums", 2),
            ("nose bleeding", 2),
        ],
        "medicines": [
            "ONLY Paracetamol (500 mg) every 6-8 hours for fever — nothing else for pain without a doctor",
            "Drink a lot of fluids: ORS, coconut water, tender fluids, plain water (at least 2-3 litres a day)",
            "Complete bed rest",
        ],
        "precautions": [
            "NEVER take aspirin, ibuprofen, diclofenac or other pain-killers — they increase bleeding risk",
            "Do not wait for fever to subside — fluid intake is more important",
            "Watch for danger signs while fever is coming down (days 3-7)",
        ],
        "diet": [
            "Coconut water, ORS, rice kanji, soup — small frequent meals",
            "Rest completely even if you feel better",
        ],
        "when_doctor": [
            "GO TO HOSPITAL IMMEDIATELY if: severe stomach pain, repeated vomiting, bleeding from nose/gums, black stools, cold clammy skin, dizziness on standing, reduced urine",
            "Fever lasts more than 3 days — get a blood test (platelet + dengue test)",
        ],
    },

    "typhoid": {
        "name": "Typhoid",
        "symptoms": [
            ("continuous high fever", 3),
            ("headache", 2),
            ("loss of appetite", 2),
            ("weakness", 2),
            ("stomach pain", 2),
            ("constipation", 1),
            ("diarrhea", 1),
        ],
        "medicines": [
            "Antibiotics ONLY after a doctor confirms typhoid (blood/Widal test) — never self-medicate",
            "Paracetamol (500 mg) for fever as temporary relief",
            "ORS with every loose stool and plenty of boiled water",
        ],
        "precautions": [
            "Boil drinking water or use clean filtered water; wash fruits and vegetables well",
            "Wash hands with soap after toilet and before food",
            "Do not stop antibiotics halfway — finish the full course the doctor gives",
        ],
        "diet": [
            "Soft, boiled food: dal khichdi, curd rice, ripe banana, boiled potato",
            "Avoid raw salads, unpeeled fruits, spicy and oily food during illness",
        ],
        "when_doctor": [
            "Fever lasting more than 5-7 days even after home care — get a blood test",
            "Very high fever, confusion, severe stomach pain, or blood in stool",
            "Typhoid usually needs a doctor's prescription — do not treat at home alone",
        ],
    },

    "food_poisoning": {
        "name": "Gastroenteritis / Food Poisoning",
        "symptoms": [
            ("diarrhea", 3),
            ("vomiting", 3),
            ("stomach pain", 2),
            ("abdominal cramps", 2),
            ("nausea", 2),
            ("weakness", 2),
            ("fever", 1),
        ],
        "medicines": [
            "ORS (1 packet in 1 litre clean water) after every loose stool — the most important treatment",
            "Zinc tablets (for children) as per doctor to shorten diarrhoea",
            "Paracetamol only if there is fever",
            "Continue eating — do not stay empty stomach",
        ],
        "precautions": [
            "Do NOT use anti-diarrhoea (stopping) medicines if there is fever or blood in stool",
            "Avoid milk, oily, spicy, and street food for a couple of days",
            "Drink only boiled or filtered water",
        ],
        "diet": [
            "Banana, rice, apple, toast diet (the BRAT diet) once vomiting stops",
            "Coconut water and ORS to replace lost salts",
        ],
        "when_doctor": [
            "Blood in stool, very high fever, or severe continuous stomach pain",
            "Signs of dehydration: no urine for 6-8 hours, very dry mouth, sunken eyes, dizziness on standing",
            "Vomiting that does not stop, so no water stays down for more than a few hours",
            "The sick person is a child, elderly, or pregnant — see a doctor sooner",
        ],
    },

    "acid_reflux": {
        "name": "Acidity / Gastritis (Acid Reflux)",
        "symptoms": [
            ("heartburn", 2),
            ("acidity", 2),
            ("bloating", 2),
            ("stomach pain", 2),
            ("nausea", 1),
            ("bad taste in mouth", 1),
        ],
        "medicines": [
            "Simple antacid (as per its directions) for temporary relief of burning",
            "Do not lie down for at least 1-2 hours after eating",
            "Sleep with the head slightly raised if night-time burning bothers you",
        ],
        "precautions": [
            "Avoid very spicy, oily, fried food, tea/coffee on empty stomach, and tobacco",
            "Eat small meals, not one big meal",
            "Do not eat at least 3 hours before sleeping",
            "Do not take pain medicines (aspirin/ibuprofen) repeatedly — they increase acidity and can cause ulcers",
        ],
        "diet": [
            "Plain rice, curd, vegetables, buttermilk, banana, melon",
            "Warm water through the day instead of cold drinks",
        ],
        "when_doctor": [
            "Burning pain that is not relieved by antacid, or happens often (more than twice a week)",
            "Black/tarry stools, vomiting blood, or sudden severe stomach pain",
            "Trouble swallowing food or weight loss without trying",
            "If you are over 45 and this is a new problem — get it checked",
        ],
    },

    "anemia": {
        "name": "Anemia (Low Blood / Weakness due to low haemoglobin)",
        "symptoms": [
            ("fatigue", 3),
            ("weakness", 3),
            ("dizziness", 2),
            ("shortness of breath", 2),
            ("pale skin", 2),
            ("pale nails", 1),
            ("headache", 1),
            ("palpitations", 1),
        ],
        "medicines": [
            "Iron and folic acid tablets — but only after a blood test shows low haemoglobin",
            "Albendazole deworming tablet twice a year if worm infection is likely (ask the health centre)",
            "Vitamin C (lemon, amla) with iron-rich food to help absorption",
        ],
        "precautions": [
            "Do not take iron tablets with tea, coffee, or milk — take with water/C-vitamin",
            "Keep iron tablets away from children — overdose is dangerous",
            "Find and treat the cause (worm, poor diet, bleeding) — tablets alone may not be enough",
        ],
        "diet": [
            "Green leafy vegetables (palak, methi), jaggery, dates, peanuts, millets (ragi), beans",
            "Cooking in iron utensils adds some iron to food",
            "Include lemon or amla with meals to absorb iron better",
        ],
        "when_doctor": [
            "Get a haemoglobin test at a health centre for a proper diagnosis",
            "Very pale palms, fast heartbeat, breathlessness on small effort, or fainting",
            "Pregnant women and young children with anemia need monthly follow-up",
        ],
    },

    "hypertension": {
        "name": "High Blood Pressure (Hypertension)",
        "symptoms": [
            ("headache", 2),
            ("dizziness", 2),
            ("nose bleeding", 1),
            ("blurred vision", 1),
            ("palpitations", 1),
        ],
        "medicines": [
            "BP medicines must be started, adjusted, and continued ONLY by a doctor — never self-medicate",
            "Check BP at a health centre or with a home monitor regularly if advised",
        ],
        "precautions": [
            "Reduce salt to less than a teaspoon (5 g) a day — less is best",
            "Avoid tobacco and alcohol; quit smoking completely",
            "Walk/exercise at least 30 minutes a day",
            "Do not stop BP medicines on your own once started, and never take a double dose if a dose is missed",
        ],
        "diet": [
            "Less salt in all food; avoid pickles, papad, packaged snacks, and processed food",
            "More fruits, vegetables, whole grains, and dals; limit ghee/oil",
        ],
        "when_doctor": [
            "Get BP checked at a health centre — it usually has no symptoms so a check is needed",
            "Severe headache, blurred vision, chest pain, or breathing trouble with high BP — go to hospital",
            "Any reading above 180/110 needs quick medical attention",
        ],
    },

    "diabetes": {
        "name": "Type 2 Diabetes (Sugar)",
        "symptoms": [
            ("excessive thirst", 2),
            ("frequent urination", 2),
            ("excessive hunger", 2),
            ("slow healing of wounds", 2),
            ("weight loss", 1),
            ("fatigue", 1),
            ("blurred vision", 1),
        ],
        "medicines": [
            "Medicines as prescribed after a blood sugar test — never buy/start sugar tablets on your own",
            "For very high sugar, a doctor may prescribe insulin — follow the dose exactly",
        ],
        "precautions": [
            "Test fasting blood sugar at a health centre to confirm diagnosis",
            "Cut sugar, sweets, sweet drinks, and limit rice/chapati amount",
            "Walk 30-40 minutes daily; keep feet clean and dry and check for painless wounds",
            "Do not skip medicines; keep them protected from heat",
        ],
        "diet": [
            "Whole grains, lots of vegetables, dal, sprouts, fruits like guava and apple in small amounts",
            "Avoid sugar, honey, jaggery, cold drinks, sweets, and fried snacks",
        ],
        "when_doctor": [
            "Visit the health centre for blood sugar testing if you have thirst + frequent urination + tiredness",
            "Sugar tests are important for anyone above 30 with family history of diabetes",
            "Extreme weakness, vomiting, belly pain, rapid breathing, or a wound that is not healing — hospital immediately",
        ],
    },

    "bronchitis": {
        "name": "Bronchitis (Acute)",
        "symptoms": [
            ("cough", 3),
            ("cough with phlegm", 2),
            ("chest tightness", 2),
            ("shortness of breath", 2),
            ("wheezing", 2),
            ("fever", 1),
            ("fatigue", 1),
        ],
        "medicines": [
            "Warm water and steam inhalation to loosen phlegm — 2-3 times a day",
            "Plenty of rest and fluids",
            "Most acute bronchitis is viral and needs no antibiotic — antibiotics are for cases confirmed by a doctor",
        ],
        "precautions": [
            "Avoid smoke, dust, and smoke from cooking (breathe away from the stove)",
            "Avoid cold drinks and cold air; cover the mouth in dust",
            "Do not smoke, and do not let anyone smoke near the patient",
        ],
        "diet": [
            "Warm soups, honey with warm water, and easy food like khichdi",
            "Drink warm fluids throughout the day to thin the phlegm",
        ],
        "when_doctor": [
            "Cough with breathlessness, high fever, or blood in the phlegm",
            "Cough lasting more than 3 weeks",
            "Very fast breathing, bluish lips, or sleepiness — hospital immediately",
        ],
    },

    "pneumonia": {
        "name": "Pneumonia",
        "symptoms": [
            ("high fever", 3),
            ("fast breathing", 3),
            ("shortness of breath", 3),
            ("chills", 3),
            ("cough", 2),
            ("chest pain", 2),
            ("fatigue", 2),
        ],
        "medicines": [
            "This condition needs medical treatment — antibiotics may be needed and must be given by a doctor",
            "Paracetamol for fever as temporary relief while arranging to see a doctor",
            "Keep the patient resting, sitting up slightly for easier breathing",
        ],
        "precautions": [
            "Do NOT delay — this can become serious quickly, especially in children and elders",
            "Do not attempt to treat pneumonia only at home",
        ],
        "diet": [
            "Give small frequent sips of water to keep hydrated",
            "Light warm food if the patient can eat",
        ],
        "when_doctor": [
            "SEE A DOCTOR OR GO TO THE HOSPITAL the same day if high fever + fast/difficult breathing + chest pain",
            "Children breathing faster than 40 breaths/min or chest pulling in while breathing — urgent",
            "Bluish lips or face, confusion, or not drinking anything — this is an emergency",
        ],
    },

    "tuberculosis": {
        "name": "Tuberculosis (TB)",
        "symptoms": [
            ("prolonged cough", 3),
            ("coughing up blood", 3),
            ("night sweats", 3),
            ("weight loss", 3),
            ("fever", 2),
            ("fatigue", 2),
            ("chest pain", 1),
        ],
        "medicines": [
            "TB medicine course from a government health centre (DOTS) is FREE — go to the centre, but ONLY the doctor prescribes the drugs",
            "Paracetamol for fever temporarily",
        ],
        "precautions": [
            "Cover the mouth while coughing and do not spit in the open",
            "Give the full 6-month TB course without stopping — stopping early creates drug-resistant TB",
            "The whole family should get checked if someone coughs with these symptoms",
            "Good food is part of the treatment — make sure the patient eats well",
        ],
        "diet": [
            "High-protein food: dal, eggs, milk, peanuts, sprouts — TB recovery needs good food",
            "Eat frequent small meals if appetite is poor",
        ],
        "when_doctor": [
            "Cough lasting more than 3 WEEKS with fever, night sweating, or weight loss — get sputum test at the health centre",
            "Coughing up blood — see a doctor immediately",
        ],
    },

    "conjunctivitis": {
        "name": "Conjunctivitis (Pink Eye)",
        "symptoms": [
            ("redness in eyes", 3),
            ("watery eyes", 3),
            ("eye discharge", 2),
            ("itching", 2),
            ("eye swelling", 1),
        ],
        "medicines": [
            "Clean the eye gently with a clean, wet cloth — wipe from inner corner outward, use a fresh cloth each time",
            "Cool compress (clean cloth with cold water) 2-3 times a day for swelling and itching",
            "Lubricating eye drops, or antibiotic drops ONLY if a doctor prescribes them",
        ],
        "precautions": [
            "Do not share towels, handkerchiefs, or pillows — it spreads easily",
            "Do not rub the eyes or touch others; wash hands often",
            "Do not put breast milk, urine, or other home 'drops' in the eye — they cause more infection",
            "The patient can attend school/work after discharge stops",
        ],
        "diet": [
            "A normal diet; keep hands and face clean",
        ],
        "when_doctor": [
            "Eye pain, blurred vision, or sensitivity to light — NOT just redness",
            "Thick yellow/green discharge that does not settle, or redness lasting more than a week",
            "Redness after an injury to the eye, or in a newborn baby",
        ],
    },

    "uti": {
        "name": "Urinary Tract Infection (UTI)",
        "symptoms": [
            ("burning pain while urinating", 3),
            ("frequent urination", 2),
            ("urgent urination", 2),
            ("cloudy urine", 2),
            ("stomach pain", 1),
            ("fever", 1),
        ],
        "medicines": [
            "Drink plenty of water through the day (this is very important)",
            "Do not hold urine — go when you feel the need",
            "Antibiotics ONLY after a doctor confirms — urine infection usually needs a short antibiotic course",
        ],
        "precautions": [
            "Keep the area clean and dry; females should wipe from front to back",
            "Wear clean, loose cotton underwear; avoid holding urine for long hours",
            "Do NOT take antibiotics bought on your own — wrong or repeated doses make infection resistant",
        ],
        "diet": [
            "Plenty of water and fluids through the day (aim for at least 2 litres)",
            "Fresh lime water and coconut water are helpful",
        ],
        "when_doctor": [
            "Burning/pain while urinating that does not settle in a day, or comes with fever",
            "Blood in urine or very foul-smelling urine",
            "Pregnant women and children with these symptoms must see a doctor the same day",
            "Back pain with fever (may mean kidney infection) — see a doctor promptly",
        ],
    },

    "migraine": {
        "name": "Migraine (Severe Headache)",
        "symptoms": [
            ("throbbing headache", 2),
            ("one-sided headache", 2),
            ("nausea", 2),
            ("sensitivity to light", 2),
            ("blurred vision", 1),
        ],
        "medicines": [
            "Paracetamol (500 mg) early in the attack, at the very start of the pain, at the doctor's recommended dose",
            "Rest in a quiet, dark room",
            "Cold or warm cloth on the head and neck",
        ],
        "precautions": [
            "Keep a trigger diary: fasting, less sleep, certain foods and stress are common triggers; avoid yours",
            "Do not skip meals and do not miss sleep",
            "Do not take pain-killers too often (more than 2 days a week) — overuse itself causes headaches",
        ],
        "diet": [
            "Regular meals on time; drink enough water",
            "Avoid known trigger foods (often cheese, chocolate, excess coffee/tea)",
        ],
        "when_doctor": [
            "The worst headache of your life, or sudden thunderclap headache — hospital immediately",
            "Headache with fever + stiff neck, fits, weakness of a limb, or confusion",
            "Headache that keeps you from daily work more than a few days a month",
            "Frequent headaches after injury to the head",
        ],
    },

    "chickenpox": {
        "name": "Chickenpox",
        "symptoms": [
            ("itchy skin rash", 3),
            ("blisters", 3),
            ("skin rash", 2),
            ("fever", 1),
            ("fatigue", 1),
        ],
        "medicines": [
            "Paracetamol for fever (only if fever is there) — temporary relief",
            "Calamine lotion on the blisters to reduce itching",
            "Keep nails trimmed and hands clean to avoid scratching",
        ],
        "precautions": [
            "Keep the sick person away from children, pregnant women, and elders during the rash days",
            "Do NOT scratch and break blisters — that causes infection and scars",
            "Do not give aspirin to children (Reye's syndrome risk)",
            "Bathe gently with plain water; keep the body clean",
        ],
        "diet": [
            "Soft, cool food and plenty of fluids",
            "Avoid very spicy food that irritates the mouth sores",
        ],
        "when_doctor": [
            "Blister areas become painful, red, and oozing (skin infection)",
            "High fever, severe headache, breathing trouble, or drowsiness",
            "The sick person is pregnant, a newborn, or has weak immunity",
        ],
    },

    "skin_fungal": {
        "name": "Fungal Skin Infection (Ringworm / Dhobi's itch)",
        "symptoms": [
            ("itchy skin rash", 3),
            ("ring-shaped rash", 2),
            ("skin redness", 2),
            ("flaking skin", 2),
        ],
        "medicines": [
            "Antifungal cream from the pharmacy (e.g., clotrimazole) applied a little beyond the rash edge, as per its instructions",
            "Keep the area clean and dry; do not scratch",
            "Wash clothes, towels, and underclothes daily in hot water and dry in the sun",
        ],
        "precautions": [
            "Apply cream for at least 2-4 weeks even after the rash looks better — stopping early causes it to come back",
            "Do not share towels, clothing, or combs",
            "Wear loose cotton clothes; change wet clothes promptly",
        ],
        "diet": [
            "A normal diet; reduce too much sugar if you are diabetic",
        ],
        "when_doctor": [
            "Rash that does not improve after 2 weeks of cream, or spreads fast",
            "If you have diabetes or weak immunity and get a fungal infection",
            "Rash with pus, fever, or severe pain",
        ],
    },

    "appendicitis_alert": {
        "name": "Suspected Appendicitis (Needs Immediate Doctor)",
        "symptoms": [
            ("severe stomach pain", 3),
            ("pain moving to lower right side", 3),
            ("vomiting", 2),
            ("fever", 2),
            ("loss of appetite", 2),
        ],
        "medicines": [],
        "precautions": [
            "DO NOT eat or drink anything — keep the stomach empty for the doctor",
            "DO NOT take pain-killers — they can hide the pain and delay the doctor's judgement",
            "Do NOT apply heat on the belly",
        ],
        "diet": [
            "Nothing to eat or drink until a doctor examines (go empty-stomach)",
        ],
        "when_doctor": [
            "Severe stomach pain starting near the navel and moving to the lower RIGHT side with vomiting/fever — go to the nearest doctor or hospital NOW",
            "Pain that gets worse with time and makes walking or pressing the belly very painful",
        ],
    },
}

# Aliases that map common user words/phrases to diseases (word-boundary match)
DISEASE_ALIASES = {
    "common_cold": ["cold", "common cold"],
    "influenza": ["flu", "influenza"],
    "viral_fever": ["viral fever"],
    "malaria": ["malaria"],
    "dengue": ["dengue"],
    "typhoid": ["typhoid"],
    "food_poisoning": ["food poisoning", "stomach infection", "loose motion problem"],
    "acid_reflux": ["acidity", "acid reflux", "gastritis", "gas problem"],
    "anemia": ["anemia", "anaemia", "low blood", "low hemoglobin"],
    "hypertension": ["high bp", "bp", "blood pressure", "hypertension"],
    "diabetes": ["diabetes", "sugar", "high sugar", "diabetic"],
    "bronchitis": ["bronchitis"],
    "pneumonia": ["pneumonia"],
    "tuberculosis": ["tb", "tuberculosis"],
    "conjunctivitis": ["conjunctivitis", "pink eye", "eye infection", "red eye"],
    "uti": ["uti", "urine infection", "urinary infection"],
    "migraine": ["migraine"],
    "chickenpox": ["chickenpox", "chicken pox"],
    "skin_fungal": ["ringworm", "fungal infection", "fungal skin infection"],
    "appendicitis_alert": ["appendicitis"],
}

# Aliases that map user symptom words/phrases to a canonical symptom.
# The canonical phrase must match what is written in the disease "symptoms".
SYMPTOM_ALIASES = {
    "fever": "fever",
    "temperature": "fever",
    "high fever": "high fever",
    "very high fever": "high fever",
    "fever with chills": "fever with chills",
    "fever and chills": "fever with chills",
    "cold fever": "fever with chills",
    "chills": "chills",
    "shivering": "chills",
    "sweating after fever": "sweating after fever",
    "sweating and fever": "sweating after fever",
    "mild fever": "mild fever",
    "low fever": "mild fever",
    "continuous fever": "continuous high fever",
    "fever for many days": "continuous high fever",
    "fever for a week": "continuous high fever",

    "headache": "headache",
    "head pain": "headache",
    "severe headache": "severe headache behind eyes",
    "pain behind eyes": "severe headache behind eyes",
    "pain behind the eyes": "severe headache behind eyes",
    "throbbing headache": "throbbing headache",
    "pulsing headache": "throbbing headache",
    "headache on one side": "one-sided headache",
    "one side headache": "one-sided headache",

    "body ache": "body ache",
    "body pain": "body ache",
    "muscle pain": "body ache",
    "joint pain": "joint pain",
    "joints pain": "joint pain",

    "cough": "cough",
    "dry cough": "dry cough",
    "wet cough": "cough with phlegm",
    "cough with phlegm": "cough with phlegm",
    "cough with sputum": "cough with phlegm",
    "cough for a month": "prolonged cough",
    "cough for 3 weeks": "prolonged cough",
    "cough for many weeks": "prolonged cough",
    "blood in cough": "coughing up blood",
    "coughing blood": "coughing up blood",
    "blood in sputum": "coughing up blood",
    "wheezing": "wheezing",
    "breath sound": "wheezing",

    "sore throat": "sore throat",
    "throat pain": "sore throat",
    "throat infection": "sore throat",
    "runny nose": "runny or stuffy nose",
    "stuffy nose": "runny or stuffy nose",
    "blocked nose": "runny or stuffy nose",
    "nasal block": "runny or stuffy nose",
    "sneezing": "sneezing",

    "fatigue": "fatigue",
    "tiredness": "fatigue",
    "tired all the time": "fatigue",
    "weakness": "weakness",
    "body weakness": "weakness",
    "low energy": "fatigue",

    "nausea": "nausea",
    "feeling like vomiting": "nausea",
    "vomiting": "vomiting",
    "vomit": "vomiting",
    "throwing up": "vomiting",

    "diarrhea": "diarrhea",
    "diarrhoea": "diarrhea",
    "loose motions": "diarrhea",
    "loose stools": "diarrhea",
    "watery stools": "diarrhea",
    "constipation": "constipation",

    "stomach pain": "stomach pain",
    "belly pain": "stomach pain",
    "abdominal pain": "stomach pain",
    "pain in stomach": "stomach pain",
    "severe stomach pain": "severe stomach pain",
    "stomach cramps": "abdominal cramps",
    "abdominal cramps": "abdominal cramps",
    "cramps": "abdominal cramps",
    "lower right pain": "pain moving to lower right side",
    "pain in lower right": "pain moving to lower right side",
    "pain on right side of stomach": "pain moving to lower right side",
    "bloating": "bloating",
    "gas and bloating": "bloating",
    "acidity problem": "acidity",
    "heartburn": "heartburn",
    "burning in chest": "heartburn",
    "chest pain": "chest pain",
    "chest tightness": "chest tightness",
    "tight chest": "chest tightness",
    "bad taste in mouth": "bad taste in mouth",
    "sour taste": "bad taste in mouth",
    "acid taste": "bad taste in mouth",

    "loss of appetite": "loss of appetite",
    "no appetite": "loss of appetite",
    "not feeling hungry": "loss of appetite",
    "excessive thirst": "excessive thirst",
    "very thirsty": "excessive thirst",
    "drinking too much water": "excessive thirst",
    "excessive hunger": "excessive hunger",
    "always hungry": "excessive hunger",

    "frequent urination": "frequent urination",
    "passing urine often": "frequent urination",
    "urgent urination": "urgent urination",
    "urge to urinate": "urgent urination",
    "burning while urinating": "burning pain while urinating",
    "burning urine": "burning pain while urinating",
    "pain while urinating": "burning pain while urinating",
    "pain in urine": "burning pain while urinating",
    "cloudy urine": "cloudy urine",
    "white urine": "cloudy urine",

    "weight loss": "weight loss",
    "losing weight": "weight loss",
    "night sweats": "night sweats",
    "sweating at night": "night sweats",

    "shortness of breath": "shortness of breath",
    "breathlessness": "shortness of breath",
    "difficulty breathing": "shortness of breath",
    "hard to breathe": "shortness of breath",
    "fast breathing": "fast breathing",
    "rapid breathing": "fast breathing",
    "palpitations": "palpitations",
    "fast heartbeat": "palpitations",
    "heart beating fast": "palpitations",
    "dizziness": "dizziness",
    "giddiness": "dizziness",
    "lightheaded": "dizziness",

    "nose bleeding": "nose bleeding",
    "nose bleed": "nose bleeding",
    "bleeding nose": "nose bleeding",
    "bleeding gums": "bleeding gums",
    "gums bleeding": "bleeding gums",

    "skin rash": "skin rash",
    "rash": "skin rash",
    "red spots": "skin rash",
    "itching": "itching",
    "itchy": "itching",
    "itchy skin": "itchy skin rash",
    "itchy rash": "itchy skin rash",
    "itchy skin rash": "itchy skin rash",
    "skin redness": "skin redness",
    "red patch on skin": "skin redness",
    "flaking skin": "flaking skin",
    "skin peeling": "flaking skin",
    "ring-shaped rash": "ring-shaped rash",
    "ring shaped patch": "ring-shaped rash",
    "blisters": "blisters",
    "small blisters": "blisters",
    "water blisters": "blisters",

    "redness in eyes": "redness in eyes",
    "red eye": "redness in eyes",
    "red eyes": "redness in eyes",
    "pink eye": "redness in eyes",
    "watery eyes": "watery eyes",
    "eye discharge": "eye discharge",
    "eyes stuck": "eye discharge",
    "discharge from eye": "eye discharge",
    "eye swelling": "eye swelling",
    "swollen eyes": "eye swelling",
    "blurred vision": "blurred vision",
    "vision problem": "blurred vision",
    "sensitivity to light": "sensitivity to light",
    "light hurts eyes": "sensitivity to light",

    "pale skin": "pale skin",
    "paleness": "pale skin",
    "pale nails": "pale nails",
    "pale hands": "pale skin",
    "slow healing of wounds": "slow healing of wounds",
    "wound not healing": "slow healing of wounds",
}