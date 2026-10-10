from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from pypdf import PdfReader
import re
from io import BytesIO

app = Flask(__name__)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_keywords(text):
    text = clean_text(text)

    if not text:
        return []

    tfidf = TfidfVectorizer(
        max_features=5000,
        stop_words="english",
        ngram_range=(1, 1),
        dtype=float
    )

    matrix = tfidf.fit_transform([text])
    words = tfidf.get_feature_names_out()
    scores = matrix.toarray()[0]

    top_indices = scores.argsort()[::-1][:15]

    keywords = [
        {
            "word": words[i],
            "score": round(float(scores[i]), 4)
        }
        for i in top_indices
        if scores[i] > 0
    ]

    return keywords

@app.route("/", methods=["GET", "POST"])
def home():
    keywords = []
    error = ""

    if request.method == "POST":
        uploaded_file = request.files.get("paper")

        if not uploaded_file or not uploaded_file.filename:
            error = "Please upload a research paper PDF."
        elif not uploaded_file.filename.lower().endswith(".pdf"):
            error = "Only PDF files are allowed."
        else:
            try:
                pdf_data = uploaded_file.read()

                if not pdf_data:
                    error = "The uploaded file is empty."
                else:
                    reader = PdfReader(BytesIO(pdf_data))

                    if reader.is_encrypted:
                        error = "Password-protected PDFs are not supported."
                    else:
                        text = " ".join(
                            page.extract_text() or ""
                            for page in reader.pages
                        )

                        if not text.strip():
                            error = (
                                "No readable text found. "
                                "Please upload a text-based PDF."
                            )
                        else:
                            keywords = extract_keywords(text)

                            if not keywords:
                                error = "Could not extract keywords from this PDF."

            except Exception:
                error = (
                    "Could not read this PDF. "
                    "Please upload a valid, readable PDF file."
                )

    return render_template(
        "index.html",
        keywords=keywords,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
