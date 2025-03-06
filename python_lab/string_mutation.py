import spacy
import re
import json


def load_nlp_model():
    """Load the spaCy NLP model for text processing."""
    return spacy.load("en_core_web_sm")


def detect_headings(text):
    """Detects potential headings and subheadings in text based on capitalization and structure."""
    lines = text.split("\n")
    formatted_text = ""

    for line in lines:
        line = line.strip()
        if re.match(r'^[A-Z][A-Z\s]+$', line) and len(line.split()) < 10:
            formatted_text += f"\n# {line}\n"
        elif re.match(r'^[0-9]+\.', line):
            formatted_text += f"\n## {line}\n"
        else:
            formatted_text += f"{line} "

    return formatted_text.strip()


def format_text(text, nlp):
    """Applies advanced NLP-based formatting for better structuring."""
    text = text.replace("\uf0b7", "- ")  # Fix bullet points
    text = detect_headings(text)
    text = re.sub(r"\n{2,}", "\n\n", text)  # Ensure proper spacing

    # Use NLP for sentence segmentation
    doc = nlp(text)
    formatted_sentences = "\n".join([sent.text.strip() for sent in doc.sents])

    return formatted_sentences


def process_text_file(input_file, output_file):
    """Reads a raw text file, applies NLP-based formatting, and saves structured output."""
    nlp = load_nlp_model()

    with open(input_file, "r", encoding="utf-8") as file:
        raw_text = file.read()

    formatted_text = format_text(raw_text, nlp)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(formatted_text)

    print(f"Formatted text saved to {output_file}")

# Example usage
process_text_file(r"C:\Users\adity\OneDrive\Desktop\New Text Document (2).txt", "formatted_text.txt")
