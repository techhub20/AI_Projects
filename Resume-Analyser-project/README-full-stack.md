
# Resume Analyzer - Full Stack Solution

This is a full-stack solution for the **Resume Analyzer** application. It includes three main projects:

1. **Frontend**: Angular-based UI for the Resume Analyzer.
2. **Backend AI Service**: Python Flask-based AI service to analyze resumes.
3. **Backend Java Service**: Java Spring Boot-based service for the backend API.

Docker Compose is used to manage and orchestrate the containers for all three services.

---

## Features

-  Upload resumes and job descriptions via the UI
-  Resume analysis with skills and domain matching
-  Generate recommendations based on job requirements
-  CORS-enabled communication between frontend and backend services
- Dockerized environment for easy setup and deployment

---

##  Tech Stack

- **Frontend (Angular)**
  - Angular 14+
  - CSS for styling

- **Backend AI Service (Flask)**
  - Python 3.12
  - Flask
  - Flask-CORS for enabling CORS between frontend and backend
  - PDF, DOCX text extraction (pdfminer, python-docx)
  - NLP-based keyword matching

- **Backend Java Service (Spring Boot)**
  - Java 17+
  - Spring Boot
  - REST API for handling backend services

- **Docker** for containerization
- **Docker Compose** for multi-container orchestration

---

## Getting Started

### 1. Clone the Repo

Clone the repository to your local machine:

```bash
git clone https://github.com/techhub20/resume-analyzer-project.git
cd resume-analyzer-project
```

### 2. Docker Compose Setup

#### Build and Run All Services with Docker Compose

This project uses Docker Compose to run all three services (Frontend, Flask Backend, and Java Spring Boot Backend) in separate containers.

```bash
 docker ps
 
 docker-compose up --build

#### If required to stop and remove existing containers
 docker compose down -v
```


This will:
- Build Docker images for all three services.
- Start the containers for the Angular frontend, Flask backend, and Java Spring Boot backend.

The services will be available at the following URLs:
- **Frontend**: http://localhost:4200
- **Flask AI Backend**: http://localhost:5000
- **Java Spring Boot Backend**: http://localhost:8080

### 3. Access the Application

- Open your browser and go to [http://localhost:4200](http://localhost:4200) to access the **Angular UI**.
- The frontend will interact with the **Flask AI Backend** (at port 5000) to analyze resumes.
- The **Java Spring Boot Backend** (at port 8080) provides additional services (e.g., user management, authentication) to the overall application.

---

## API Usage

### Flask AI Service API

- **POST /analyze**
  - **Request**: 
    - `resume` (File upload, .pdf or .docx)
    - `job_description` (String of job description)
  - **Response**:
    ```json
    {
      "score": 94,
      "missing_keywords": {
        "skills": [],
        "domains": ["docker", "cloud platform"]
      },
      "recommendations": {
        "general": "Good match! Your resume covers most requirements.",
        "keywords": ["cloud", "preferred", "join"]
      }
    }
    ```

### Java Spring Boot API

- **POST /submitResume**
  - **Request**:
    - `resume` (File upload, .pdf or .docx)
    - `job_description` (String of job description)
  - **Response**:
    ```json
    {
      "status": "success",
      "message": "Resume successfully submitted for analysis."
    }
    ```

---

## Project Structure

```
resume-analyzer-full-stack/
├── angular-frontend/               # Angular frontend project
├── flask-ai-backend/               # Flask AI backend project
├── java-springboot-backend/        # Java Spring Boot backend project
├── docker-compose.yml              # Docker Compose configuration for all services
└── README.md                       # This file
```

---

## Development

### Frontend (Angular)

- Navigate to the `angular-frontend` directory:
  ```bash
  cd angular-frontend
  ```
- Install dependencies:
  ```bash
  npm install
  ```
- Run the frontend locally:
  ```bash
  ng serve
  ```

### Flask AI Service Backend

- Navigate to the `flask-ai-backend` directory:
  ```bash
  cd flask-ai-backend
  ```
- Install Python dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run the backend locally:
  ```bash
  python app.py
  ```

### Java Spring Boot Backend

- Navigate to the `java-springboot-backend` directory:
  ```bash
  cd java-springboot-backend
  ```
- Build and run the Spring Boot project:
  ```bash
  ./mvnw spring-boot:run
  ```

---

## Troubleshooting

- Ensure Docker is installed and running before starting the services.
- Check that all services are properly running by visiting the appropriate URLs (Frontend: 4200, Flask: 5000, Java: 8080).
- Check logs for any errors:
  ```bash
  docker-compose logs
  ```

---
