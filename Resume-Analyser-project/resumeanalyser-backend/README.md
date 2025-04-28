
# Resume Analyzer - Java Spring Boot Backend

This is the backend API service for the **Resume Analyzer** application built with **Java Spring Boot**. It receives a resume and a job description, analyzes how well the resume matches the job, and returns relevant match scores, missing keywords, and suggestions.

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

- **Java 17+**
- **Spring Boot** – backend framework
- **Apache POI / PDFBox** – text extraction from documents
- **NLP** – basic keyword matching & contextual parsing
- **Spring Web** – REST API development
- **Spring Boot DevTools** – auto-reloading for development

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/techhub20/resume-analyzer-java-backend.git
cd resume-analyzer-java-backend
```

### 2. Install Java and Maven

Make sure you have **Java 17+** and **Maven** installed on your machine.

To check Java version:

```bash
java -version
```

To check Maven version:

```bash
mvn -v
```

### 3. Build the Project

Use Maven to install dependencies and build the project.

```bash
mvn clean install
```

### 4. Run the Server

```bash
mvn spring-boot:run
```

The backend will start at:
 http://127.0.0.1:8080

---

## API Usage

### POST `/analyze`

#### Request

- **resume**: Uploaded file (PDF or DOCX)
- **job_description**: Text string

##### Example Request (using `curl`):

```bash
curl -X POST http://127.0.0.1:8080/analyze   -F "resume=@my_resume.pdf"   -F "job_description=We are looking for a full-stack developer..."
```

#### Response

```json
{
  "score": 94,
  "missing_keywords": {
    "skills": [],
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

## Project Structure

```bash
resume-analyzer-java-backend/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── resumeanalyzer/
│   │   │           ├── controller/        # REST API Controllers
│   │   │           ├── service/           # Business logic
│   │   │           ├── model/             # Data models
│   │   │           └── util/              # Utility classes
│   │   ├── resources/
│   │   │   ├── application.properties     # Configuration file
├── pom.xml                                 # Maven dependencies and configurations
└── README.md                               # This file
```

---

## Recommendations

- **Improve Resume**: Based on the job description, make sure to add the missing keywords or related skills.
- **Use NLP**: Use advanced natural language processing techniques for more accurate analysis.

---
