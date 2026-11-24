
import gspread
import requests
import json
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SPREADSHEET_ID = "1jxjHdL6JhiGpqQJeQTmB6QLs9vfKXCKzmi7ITrmhKXs"

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3.5:4b"


def analyze_inquiry(inquiry):
    prompt = f"""
You are a customer support assistant for a website design business.

Analyze this customer inquiry:
{inquiry}

Return only a JSON object with exactly these fields:
- intent
- category
- priority
- suggested_reply

Use concise values.
Priority must be Low, Medium, or High.
Do not invent prices or business policies.
Make the suggested reply friendly and professional.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "format": "json",
            "think": False,
            "stream": False,
            "options": {"num_predict": 1024}
        },
        timeout=300
    )

    response.raise_for_status()

    result = response.json()
    ai_text = result.get("message", {}).get("content", "")

    if not ai_text.strip():
        raise ValueError("The AI returned an empty response.")

    return json.loads(ai_text)


def main():
    credentials = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    worksheet = spreadsheet.sheet1

    records = worksheet.get_all_values()

    if len(records) < 2:
        print("No customer inquiries found.")
        return

    row_number = len(records)
    row = records[-1]

    inquiry = row[3].strip() if len(row) > 3 else ""

    if not inquiry:
        print("The latest row has no inquiry.")
        return

    # Check AI-specific columns G and H
    existing_intent = row[6].strip() if len(row) > 6 else ""
    existing_priority = row[7].strip() if len(row) > 7 else ""

    if existing_intent and existing_priority:
        print("This inquiry has already been analyzed by AI.")
        return

    print("Analyzing customer inquiry...")
    print("Inquiry:", inquiry)

    ai_result = analyze_inquiry(inquiry)

    worksheet.update(
        range_name=f"E{row_number}:H{row_number}",
        values=[[
            ai_result["category"],
            ai_result["suggested_reply"],
            ai_result["intent"],
            ai_result["priority"]
        ]]
    )

    print("\nSUCCESS! Google Sheets has been updated.")
    print("Category:", ai_result["category"])
    print("Intent:", ai_result["intent"])
    print("Priority:", ai_result["priority"])
    print("Suggested reply:", ai_result["suggested_reply"])


if __name__ == "__main__":
    main()
