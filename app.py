from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/ipsw/<path:endpoint>", methods=["GET"])
def proxy(endpoint):
    try:
        r = requests.get(f"https://api.ipsw.me/v4/{endpoint}", timeout=10)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "✅ IPSW Proxy is running!"
