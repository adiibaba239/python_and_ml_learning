import os
import re
import requests
import fitz  # PyMuPDF for PDF integrity check

# API Endpoints (Replace with actual URLs)
LOGIN_URL = "https://paradox-study.ue.r.appspot.com/api/admin/adminLogin"
UPLOAD_URL = "https://paradox-study.ue.r.appspot.com/api/books/uploadAdminBook"

# Admin Credentials (Replace with actual credentials)
USERNAME = "aditya.dadhich.239@gmail.com"
PASSWORD = "aditya@123"

# Folder containing books
BOOKS_DIRECTORY = r"C:\Users\adity\Downloads\B.tech 2nd year CS -20250306T175144Z-001\B.tech 2nd year CS"

# Fixed Fields
BRANCH = "CS"
YEAR = "2"


def sanitize_filename(filename):
    """Replace spaces with underscores and remove special characters."""
    filename = filename.replace(" ", "_")  # Replace spaces with underscores
    filename = re.sub(r"[^\w\.-]", "", filename)  # Remove special characters except dots and dashes
    return filename


def is_valid_pdf(pdf_path):
    """Check if a PDF file is valid and can be opened."""
    try:
        with fitz.open(pdf_path) as doc:
            return len(doc) > 0  # Ensure it has pages
    except Exception as e:
        print(f"❌ Corrupt PDF: {pdf_path} ({e})")
        return False


def authenticate():
    """Authenticate and get the access token."""
    response = requests.post(LOGIN_URL, json={"email": USERNAME, "password": PASSWORD})
    if response.status_code == 200:
        return response.json().get("token")  # Adjust based on response structure
    else:
        print("Login failed:", response.text)
        return None


def upload_book(token, subject, book_name, pdf_path):
    """Upload a book to the admin panel."""
    headers = {"Authorization": f"Bearer {token}"}
    sanitized_name = sanitize_filename(book_name)

    data = {
        "branch": BRANCH,
        "name": sanitized_name,
        "year": YEAR,
        "sem": "3",  # Adjust if semester information is available
        "subject": subject,
    }

    with open(pdf_path, "rb") as pdf_file:
        files = {"book": (sanitized_name, pdf_file, "application/pdf")}
        response = requests.post(UPLOAD_URL, headers=headers, data=data, files=files)

    if response.status_code == 200:
        print(f"✅ Uploaded: {sanitized_name}")
    else:
        print(f"{sanitized_name}: {response.text}")


def process_books():
    """Iterate through subject folders and upload valid PDFs."""
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
                if is_valid_pdf(book_path):  # Check PDF integrity
                    upload_book(token, subject, book_file, book_path)
                else:
                    print(f"Skipping invalid PDF: {book_file}")


if __name__ == "__main__":
    process_books()
