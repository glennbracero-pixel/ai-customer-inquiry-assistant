
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3.5:4b"


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    inquiry = str(data.get("inquiry", "")).strip()

    if not inquiry:
        return jsonify({"error": "Inquiry is required"}), 400

    prompt = f"""
You are a customer support assistant for a website design business.

Analyze this customer inquiry:
{inquiry}

Return ONLY the final JSON object.
Do not include explanations, analysis, or thinking.
Use short values and concise sentences.

The JSON must contain exactly these fields:
- intent
- category
- priority
- suggested_reply

Do not invent prices or business policies.
Make the suggested reply friendly and professional.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "format": "json",
                "stream": False,
                "options": {
    "num_predict": 1024
}
            },
            timeout=300
        )

        response.raise_for_status()
        result = response.json()

        print("OLLAMA RESULT:", result)

        ai_text = result.get("message", {}).get("content", "")
        print("RAW AI RESPONSE:", repr(ai_text))

        if not ai_text.strip():
            return jsonify({
                "error": "Ollama returned an empty response",
                "ollama_result": result
            }), 502

        ai_data = json.loads(ai_text)
        return jsonify(ai_data)

    except requests.exceptions.RequestException as error:
        print("OLLAMA CONNECTION ERROR:", error)

        if error.response is not None:
            print("OLLAMA RESPONSE:", error.response.text)

        return jsonify({
            "error": "Could not connect to Ollama",
            "details": str(error)
        }), 502

    except (KeyError, ValueError) as error:
        print("AI RESPONSE ERROR:", error)

        return jsonify({
            "error": "Could not process the AI response",
            "details": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
