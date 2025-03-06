import os
import requests

# API Endpoints (Replace with actual URLs)
LOGIN_URL = "https://your-admin-panel.com/api/login"
UPLOAD_URL = "https://your-admin-panel.com/api/upload_book"

# Admin Credentials (Replace with actual credentials)
USERNAME = "your_username"
PASSWORD = "your_password"

# Folder containing books
BOOKS_DIRECTORY = "path/to/B.tech 2nd year CS"

# Fixed Fields
BRANCH = "Computer Science"
YEAR = "2nd Year"


def authenticate():
    """Authenticate and get the access token."""
    response = requests.post(LOGIN_URL, data={"username": USERNAME, "password": PASSWORD})
    if response.status_code == 200:
        return response.json().get("token")  # Adjust based on response structure
    else:
        print("Login failed:", response.text)
        return None


def upload_book(token, subject, book_name, pdf_path):
    """Upload a book to the admin panel."""
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "branch": BRANCH,
        "book_name": book_name,
        "year": YEAR,
        "semester": "3rd/4th",  # Adjust if semester information is available
        "subject": subject,
    }
    files = {"pdf": open(pdf_path, "rb")}

    response = requests.post(UPLOAD_URL, headers=headers, data=data, files=files)

    if response.status_code == 200:
        print(f"✅ Uploaded: {book_name}")
    else:
        print(f"❌ Failed to upload {book_name}: {response.text}")


def process_books():
    """Iterate through subject folders and upload PDFs."""
    token = authenticate()
    if not token:
        return

    for subject in os.listdir(BOOKS_DIRECTORY):
        subject_path = os.path.join(BOOKS_DIRECTORY, subject)
        if not os.path.isdir(subject_path):
            continue  # Skip if not a folder

        for book_file in os.listdir(subject_path):
            book_path = os.path.join(subject_path, book_file)
            if book_file.endswith(".pdf"):  # Ensure it's a PDF
                upload_book(token, subject, book_file, book_path)


if __name__ == "__main__":
    process_books()
