import pdfplumber
import os
from language import detect_language

def read_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_documents(folder="data"):
    docs = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            text = read_pdf(path)
        elif file.endswith(".txt"):
            text = read_txt(path)
        else:
            continue

        lang = detect_language(text)
        docs.append({
            "text": text,
            "language": lang,
            "source": file
        })

    return docs
