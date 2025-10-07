# AI on FHIR — NLQ Frontend

This project is the front-end for the AI on FHIR Take-Home Assessment.
It connects to a FastAPI backend (`http://127.0.0.1:8000`) that simulates FHIR API queries.

## Features
- Input field for natural language query
- Table of patient results
- Bar chart of patients per condition
- Error handling for invalid queries
- Fully responsive layout

## Run Locally
1. Clone or unzip the project.
2. Go to App.tsx file
3. Open one more terminal, make sure to have backend runing in new terminal screen (important! the instruction of running back end in README.md file for backend in part 1)
4. back to the first terminal of front-end:
   - Install dependencies: npm install

5. Start the development server: npm run dev

6. Ensure your backend (FastAPI) is running on port `8000`.

## Example Queries
- "show diabetic patients over 50"
- "asthma patients under 18"
- "display cancer over 60"

