from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import spacy

# Load spaCy English model (make sure you've run:
#   python -m spacy download en_core_web_sm
# )
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback to blank English if model not installed; still lets the app run.
    from spacy.lang.en import English
    nlp = English()

app = FastAPI(title="AI on FHIR - NLQ Backend (Simulated)")

# Allow local Next.js dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NLQ(BaseModel):
    query: str

# --- Simulated patient "database" ---
PATIENTS = [
    {"id":"p1","name":"Alice Chen","age":62,"condition":"diabetes"},
    {"id":"p2","name":"Bob Nguyen","age":71,"condition":"diabetes"},
    {"id":"p3","name":"Carmen Lee","age":55,"condition":"diabetes"},
    {"id":"p4","name":"Daniel Kim","age":16,"condition":"asthma"},
    {"id":"p5","name":"Evelyn Brown","age":12,"condition":"asthma"},
    {"id":"p6","name":"Farah Ali","age":43,"condition":"hypertension"},
    {"id":"p7","name":"George Patel","age":66,"condition":"hypertension"},
    {"id":"p8","name":"Dacod Romano","age":85,"condition":"cancer"},
]

# --- very lightweight parser ---
def parse_query(query: str):
    doc = nlp(query)
    q = query.lower()

    # condition keywords
    condition = None
    if "diabet" in q: condition = "diabetes"
    elif "asthma" in q: condition = "asthma"
    elif "hypertens" in q: condition = "hypertension"
    elif "cancer" in q: condition ="cancer"
    
    # age rules
    age_min: Optional[int] = None
    age_max: Optional[int] = None

    # crude numeric extraction
    numbers = [int(t.text) for t in doc if t.like_num]
    n = numbers[0] if numbers else None

    if n is not None:
        if "over" in q or "older than" in q or "age above" in q:
            age_min = n
        elif "under" in q or "younger than" in q or "below" in q:
            age_max = n
        elif "between" in q:
            # not fully implemented; keep simple for take-home
            age_min = n

    return condition, age_min, age_max

def to_fhir(condition: Optional[str], age_min: Optional[int], age_max: Optional[int]) -> Dict[str, Any]:
    """Simulated FHIR search Bundle for Patient & Condition."""
    patient_criteria = "any"
    if age_min is not None:
        patient_criteria = f"age>={age_min}"
    elif age_max is not None:
        patient_criteria = f"age<={age_max}"

    condition_criteria = f"code={condition}" if condition else "any"

    bundle = {
        "resourceType": "Bundle",
        "type": "searchset",
        "entry": [
            {"resource": {"resourceType": "Patient", "criteria": patient_criteria}},
            {"resource": {"resourceType": "Condition", "criteria": condition_criteria}},
        ],
    }
    return bundle

def simulate_rows(condition: Optional[str], age_min: Optional[int], age_max: Optional[int]):
    rows = PATIENTS
    if condition:
        rows = [r for r in rows if r["condition"] == condition]
    if age_min is not None:
        rows = [r for r in rows if r["age"] >= age_min]
    if age_max is not None:
        rows = [r for r in rows if r["age"] <= age_max]
    return rows

@app.post("/nlq")
def nlq(body: NLQ):
    condition, age_min, age_max = parse_query(body.query)

    # If we didn't understand the query, don't dump all rows.
    if condition is None and age_min is None and age_max is None:
        # Optionally you can still return the FHIR bundle if you want
        # but for a clean UX just raise an error:
        raise HTTPException(
            status_code=400,
            detail="Couldn't understand the query. Try specifying a condition (e.g., diabetes, asthma) or an age (e.g., over 50).",
        )

    fhir = to_fhir(condition, age_min, age_max)
    rows = simulate_rows(condition, age_min, age_max)
    return {"fhir": fhir, "rows": rows, "parsed": {"condition": condition, "age_min": age_min, "age_max": age_max}}
