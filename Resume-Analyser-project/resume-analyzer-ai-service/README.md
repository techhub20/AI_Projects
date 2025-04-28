# Resume Analyzer - AI Service (Flask Backend)

This is the backend API service for the **Resume Analyzer** application. It receives a resume and a job description, analyzes how well the resume matches the job, and returns relevant match scores, missing keywords, and suggestions.

---

## Features

- Accepts resume uploads in PDF, DOCX formats
- Accepts pasted job descriptions (text)
- Analyzes skill and domain match
- Extracts keywords and highlights gaps
- Returns recommendations to improve resume match
- Supports integration with Angular frontend (CORS-enabled)

---

## Tech Stack

- **Python 3.11**
- **Flask** – lightweight REST API
- **Flask-CORS** – enables frontend-backend communication
- **pdfminer / python-docx / fitz (PyMuPDF)** – text extraction from documents
- **NLP** – basic keyword matching & contextual parsing

---

## Getting Started

1. **Clone the Repo**

```bash
git clone https://github.com/techhub20/resume-analyzer-ai-service.git
cd resume-analyzer-ai-service
```

2. **Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Server**

```bash
python app.py
```

The backend will start at:  
 `http://127.0.0.1:5000`

---

## API Usage

### `POST /analyze`

**Request:**  
- **resume**: Uploaded file (PDF or DOCX)
- **job_description**: Text string of the job description

#### Example with `curl`

```bash
curl -X POST http://127.0.0.1:5000/analyze \
  -F "resume=@my_resume.pdf" \
  -F "job_description=We are looking for a full-stack developer..."
```

#### Example Response:

```json
{
  "score": 94,
  "missing_keywords": {
    "skills": "Almost all required skills matched!",
    "domains": ["docker", "cloud platform"]
  },
  "recommendations": {
    "general": "Good match! Your resume covers most requirements.",
    "keywords": [
      "cloud", "preferred", "join"
    ]
  }
}
```

---

### `GET /health`

**Request:**  
To check if the service is up and running.

#### Example with `curl`

```bash
curl http://127.0.0.1:5000/health
```

**Response:**

```json
{ "status": "ok" }
```

---

## Project Structure

```bash
resume-analyzer-ai-service/
├── app.py                  # Main Flask app
├── utils/
│   ├── extract_text.py     # Resume text extraction logic
│   └── matcher.py          # Matching and scoring logic
├── templates/              # Optional (HTML if needed)
└── requirements.txt        # Project dependencies
```

---

## Notes

- Ensure you use resumes in either PDF or DOCX format.
- The matching system is based on keyword extraction and simple contextual analysis. It can be customized for more advanced NLP-based matching.
- The backend supports CORS for integrating with the frontend (e.g., Angular).
  
---

## CORS

This API allows cross-origin requests to support integration with frontend applications by using the `Flask-CORS` library:

```python
from flask_cors import CORS
CORS(app)
```

This ensures that the frontend (running on a different port or domain) can communicate with the backend.

---

## Debugging

When running locally, Flask logs will show detailed errors. Use the following command to run the server and check the logs for debugging purposes:

```bash
python app.py
```
