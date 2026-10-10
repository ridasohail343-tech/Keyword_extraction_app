# Keyword Extraction App

A Flask-based NLP web application that extracts the top keywords from uploaded research paper PDFs using TF-IDF.

## Features
- Upload research papers in PDF format.
- Extract text from PDF files.
- Clean and preprocess text.
- Extract the top 15 keywords using TF-IDF.
- Display keywords with their TF-IDF scores.
- Handle invalid PDFs and empty files.

## Technologies Used
- Python
- Flask
- Scikit-learn
- PyPDF
- HTML
- CSS
- Natural Language Processing (NLP)

## Project Structure
```text
Keyword_extraction_app/
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ridasohail343-tech/Keyword_extraction_app.git
```

Navigate to the project folder:

```bash
cd Keyword_extraction_app
```

Install the required libraries:

```bash
pip install flask scikit-learn pypdf
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

Upload a research paper PDF and click **Extract Keywords** to view the extracted keywords and their TF-IDF scores.

## How It Works
1. The user uploads a research paper in PDF format.
2. PyPDF extracts readable text from the document.
3. The text is cleaned and preprocessed.
4. TF-IDF calculates word importance within the uploaded paper.
5. The application displays the top keywords and their scores.

## Limitations
- Supports PDF files only.
- Scanned PDFs require OCR to extract text from images.
- TF-IDF scores indicate word importance, but extracted keywords may not always represent the paper's main concepts.

## License

This project is open-source and available for educational purposes.