from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "Simplicity is the ultimate sophistication.",
    "Move fast and break things.",
    "In the middle of difficulty lies opportunity.",
    "Kill in the name of love",
    "Drink and drive",
]

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(QUOTES)})

if __name__ == "__main__":
    # 0.0.0.0 כדי שנוכל לחשוף את השרת מחוץ למכונה/קונטיינר
    app.run(host="0.0.0.0", port=5001)
