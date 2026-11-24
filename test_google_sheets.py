
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets permissions
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load your service account credentials
credentials = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

# Connect to Google Sheets
client = gspread.authorize(credentials)

# Open your spreadsheet
spreadsheet = client.open_by_key(
    "1jxjHdL6JhiGpqQJeQTmB6QLs9vfKXCKzmi7ITrmhKXs"
)

# Open the first worksheet
worksheet = spreadsheet.sheet1

# Display connection information
print("SUCCESS! Google Sheets connection is working.")
print("Spreadsheet:", spreadsheet.title)
print("Worksheet:", worksheet.title)

# Read the column headers
headers = worksheet.row_values(1)
print("Column headers:", headers)
