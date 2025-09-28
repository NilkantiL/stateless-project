from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True}), 200

@app.route("/trade/place", methods=["POST"])
def place_trade():
    # You can inspect request.json if needed
    trade_data = request.get_json(silent=True) or {}
    
    trade_id = str(uuid.uuid4())
    return jsonify({"status": "accepted", "id": trade_id}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

