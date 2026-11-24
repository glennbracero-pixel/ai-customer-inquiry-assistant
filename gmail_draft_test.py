import os
import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

CLIENT_FILE = "gmail_oauth_client.json"
TOKEN_FILE = "gmail_token.json"

MY_EMAIL = "loltv2591@gmail.com"


def connect_to_gmail():
    credentials = None

    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(
            TOKEN_FILE, SCOPES
        )

    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_FILE, SCOPES
        )
        credentials = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token_file:
            token_file.write(credentials.to_json())

    return build("gmail", "v1", credentials=credentials)


def create_test_draft(service):
    message = EmailMessage()

    message["To"] = MY_EMAIL
    message["Subject"] = "Python Gmail API Test"
    message.set_content(
        "Hello!\n\n"
        "This is a test draft created by my Python AI Customer Inquiry Assistant.\n\n"
        "This email has NOT been sent.\n"
    )

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    draft = {
        "message": {
            "raw": encoded_message
        }
    }

    result = service.users().drafts().create(
        userId="me",
        body=draft
    ).execute()

    print("SUCCESS! Your Python program created a Gmail draft.")
    print("Draft ID:", result["id"])
    print("Recipient:", MY_EMAIL)
    print("The email was NOT sent.")


if __name__ == "__main__":
    print("Connecting to Gmail...")
    gmail_service = connect_to_gmail()

    print("Gmail connection successful!")
    create_test_draft(gmail_service)