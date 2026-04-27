from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)