### **PART1:**

#### **How you run the file locally:**



1\. open the file, and Install Python

Make sure Python 3.9+ is installed (check in terminal): ***python --version***



2\. Set up a virtual environment with 2 these lines of code (in terminal)

**⦁	*python -m venv .venv***

**⦁**	Activate it:

	- For Window: **.*\\.venv\\Scripts\\Activate.ps1***

	- For Mac/Linux: ***source .venv/bin/activate***



3\. Install dependencies

**⦁	*pip install fastapi uvicorn spacy***

**⦁	*python -m spacy download en\_core\_web\_sm***



4\. Run the FastAPI app: ***uvicorn main:app --reload***





Once it starts, open your browser to: [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs)


**6 screenshots of 3 examples for queries:** https://github.com/dibatu/ai-on-fhir-fullstack/tree/main/fhir_backend/screenshots%20examples%20io%20queries

**------------------------------------------------------------------------------------------------------------------------------**



### **PART2:**

**This project is the front-end for the AI on FHIR Take-Home Assessment. It connects to a FastAPI backend (http://127.0.0.1:8000) that simulates FHIR API queries.**


**How you run the file locally:**
---

* Clone or unzip the project
* Go to App.tsx file
* Open one more terminal, make sure to have backend runing in new terminal screen (important! the instruction of running back end in README.md file for backend in part 1)
* Back to the first terminal of front-end:
* Install dependencies: ***npm install***
* Start the development server: ***npm run dev***
* Ensure your backend (FastAPI) is running on port 8000.
  

Features

* Input field for natural language query
* Table of patient results
* Bar chart of patients per condition
* Error handling for invalid queries
* Fully responsive layout





**Example Queries: 
link:** [nlq-ui/screenshots](https://github.com/dibatu/ai-on-fhir-fullstack/tree/main/nlq-ui/screenshots)



**--------------------------------------------------------------------------------------------------------------------------------**



### **PART3:**

**Security and Compliance Plan: link** https://github.com/dibatu/ai-on-fhir-fullstack/blob/main/Part3.pdf





