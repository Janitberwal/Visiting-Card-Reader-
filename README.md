
📇 Visiting Card Reader to Excel Parser

A sophisticated full-stack application that transforms physical visiting cards into structured digital data. This project employs a hybrid extraction engine combining Rule-Based systems (Regex), Natural Language Processing (SpaCy), and Large Language Models (Gemini 1.5 Flash).

🚀 The Hybrid Extraction Strategy

To ensure maximum accuracy and cost-efficiency, the project uses a tiered extraction approach:

Level 1: Rule-Based Extraction (Regex)

=>Purpose: Blazing-fast extraction of predictable patterns.

=>Used For: Phone numbers, Email addresses, and URLs.

=>Why: Regex handles these with 100% accuracy without needing an AI call.


Level 2: NLP & NER (SpaCy)

=>Purpose: Contextual understanding of entities.

=>Used For: Identifying Person Names and Locations (City/Country).

=>Why: SpaCy’s Named Entity Recognition (NER) helps distinguish between a "Company Name" and a "Person Name" by analyzing the surrounding text structure.

Level 3: Cognitive Parsing (Gemini 1.5 Flash)

=>Purpose: Handling complex layouts and "messy" OCR data.

=>Used For: Designations, Company branding, and Cross-verifying low-confidence fields.

=>Why: When text is jumbled or non-linear, the LLM acts as the "final brain" to reconstruct the data logically.

🛠️ Tech Stack

Frontend =>	React.js,  CSS Modules

Backend  =>	FastAPI (Python), Uvicorn

AI/NLP	=> Google Gemini 1.5 Flash, SpaCy (en_core_web_sm)

Data Processing	=> Regex (re), Openpyxl (Excel), Pandas

⚙️ Setup & Installation

1. Backend Setup

# Install core dependencies
pip install fastapi uvicorn google-generativeai spacy pandas openpyxl

# Download SpaCy model
python -m spacy download en_core_web_sm

# Run the server
uvicorn main.py:app --reload

2. Frontend Setup

cd card-reader-ui

npm install

npm start



