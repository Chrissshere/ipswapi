from flask import Flask, Response, jsonify
import requests

app = Flask(__name__)

@app.route("/ipsw/<path:endpoint>", methods=["GET"])
def proxy(endpoint):
    try:
        upstream_url = f"https://api.ipsw.me/v4/{endpoint}"
        r = requests.get(upstream_url, timeout=10)

        # Pass through JSON if possible
        try:
            data = r.json()
            return jsonify(data), r.status_code
        except ValueError:
            # Not JSON? Return raw text
            return Response(r.text, status=r.status_code, content_type=r.headers.get("content-type", "text/plain"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "✅ IPSW Proxy is running!"
