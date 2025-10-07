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



**Describe Workflow of An Example Input:**



1\. Frontend calls POST /nlq with { "query": "show diabetic patients over 50" }.



2.parse\_query -> returns ("diabetes", 50, None).



3.to\_fhir -> returns a Bundle with:



⦁	Patient criteria: age>=50

⦁	Condition criteria: code=diabetes



4.simulate\_rows -> filters the mock patients accordingly.



5.Response JSON includes:



⦁	parsed (for transparency),

⦁	fhir (to show your FHIR mapping),

⦁	rows (for the UI to render table/chart).





**Code lines (Main Ideas)**



1-16: the set-up environment for the application when I installed FastAPI (middleware.cors), framework baseModel from pydantric and spacy for Languages.



Next, I start title for the application and setup server through calling http://localhost:3000/docs to the browsers. 



32 -42: To users can retrieve the data of patients, i set a dataset includes very simple data about 8 patients with their ages and conditions. 



44 - 72: it is the process of parsing the query from the natural language input. it will filter to get 3 main data: patient condition, and maximum or minimum age from the query.



* In these lines of code, to understand the natural language, besides of spacy installation, I also add more the short keyword they look like typo from users such as "diabet", or "asthma" and direct them to "diabetes" or "astma". Thanks to that, we can get the more conditions of patient from user input. 



* And how the application can verify the minimum age or maximum age of patients? Yes, we also must set up the common keywords such as "over" or "under" from user input, parse them to variables correspondingly.



from 94 -102: Applies the parsed filters to the mock list. This produces the table data the frontend renders.



104- 110: Establish the structure of body request and response in server for browser.



-----------------------------------------------------------------------------------------------------------------------------------



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





