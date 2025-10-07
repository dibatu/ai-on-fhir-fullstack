# AI on FHIR – NLQ Backend (Simulated)

This is a tiny FastAPI backend that turns a natural-language query into a **simulated FHIR search** and returns **demo patient rows** suitable for the Part 2 frontend.

## 1) Prereqs
- Python 3.11+
- (Windows) Use PowerShell or Command Prompt

## 2) Setup
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\Activate
# macOS/Linux
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

# Install spaCy English model (first run only)
python -m spacy download en_core_web_sm
```

## 3) Run
```bash
uvicorn main:app --reload
```
- API docs will be at: http://127.0.0.1:8000/docs

## 4) Test
```bash
curl -X POST http://127.0.0.1:8000/nlq -H "content-type: application/json" -d "{\"query\": \"show diabetic patients over 50\"}"
```

Expected:
- A `fhir` Bundle with Patient/Condition criteria
- Filtered demo `rows` (patients), plus `parsed` fields

## 5) Notes
- This app **simulates** a FHIR search. There is no real FHIR server.
- NLP is intentionally simple for take-home clarity; you can extend `parse_query` with spaCy `Matcher`, regex rules, or a healthcare NER model.
- CORS is enabled for `http://localhost:3000` to allow the Next.js frontend to call `/nlq`.
