"""Rural Health Chatbot - Flask web application."""

import os

from flask import Flask, jsonify, render_template, request, session

from chatbot import HealthChatbot

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "rural-health-chatbot-dev-key")

bot = HealthChatbot()


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/api/start")
def api_start():
    session["state"] = {}
    return jsonify(replies=bot.greeting())


@app.post("/api/chat")
def api_chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    state = session.get("state") or {}
    # older sessions may lack the "phase" key -> engine resets it safely
    replies, state = bot.handle(state, message)
    session["state"] = state
    return jsonify(replies=replies)


@app.post("/api/reset")
def api_reset():
    session.clear()
    return jsonify(ok=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)