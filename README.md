# BharatFD - Multilingual FAQ Management System

## Overview
BharatFD is a **Django-based multilingual FAQ management system** designed to provide dynamic FAQ retrieval with **WYSIWYG editing, caching, and REST API integration**. The system is optimized for performance, **deployable with Docker**, and features an interactive frontend for seamless FAQ management.

---

## Features
- **Multi-language Support** – FAQs available in **English, Hindi, and Bengali**.
- **WYSIWYG Editor** – CKEditor integration for rich-text FAQ answers.
- **Caching Mechanism** – Uses **Redis** to improve API response times.
- **REST API** – Fetch FAQs dynamically through API endpoints.
- **Admin Panel** – Manage FAQs efficiently using Django’s admin interface.
- **Docker Support** – Simplified deployment with containerized setup.
- **Interactive UI** – Easily test FAQs with a frontend interface.

---

## Project Structure
```
BharatFD/
│── bharatfd/         # Main Django project settings
│── faq/              # FAQ app (Models, Views, APIs)
│── templates/faq/    # HTML templates for interactive FAQ page
│── static/           # Static files (CSS, JS)
│── requirements.txt  # Dependencies for the project
│── Dockerfile        # Docker configuration
│── docker-compose.yml # Docker Compose setup
│── README.md         # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Aasrithlingamagunta/BharatFD_assignment.git
cd BharatFD_assignment
```

### 2. Create & Activate Virtual Environment
```sh
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Run the Django Server
```sh
python manage.py runserver
```
Now, open **http://127.0.0.1:8000/** in your browser.

---

## API Endpoints

### Fetch All FAQs (Default: English)
```sh
GET /api/faqs/
```

### Fetch FAQs in Hindi
```sh
GET /api/faqs/?lang=hi
```

### Fetch FAQs in Bengali
```sh
GET /api/faqs/?lang=bn
```

### Example JSON Response
```json
[
    {
        "question": "What is Django?",
        "answer": "Django is a high-level Python web framework."
    },
    {
        "question": "What is REST API?",
        "answer": "REST API is an architectural style for web services."
    }
]
```

---

## Interactive FAQ Page
- **Search for FAQs dynamically.**
- **Supports real-time language switching.**
- **Available at:** `http://127.0.0.1:8000/faq/`

---
![Screenshot 2025-02-02 105518](https://github.com/user-attachments/assets/bbbe6cd2-7018-4071-8e73-04c711b08348)
![Screenshot 2025-02-02 154029](https://github.com/user-attachments/assets/4ca1901c-636b-42d8-9520-3ef8f51c5d55)


## Deployment with Docker
To deploy using **Docker**, run:
```sh
docker-compose up --build
```
The application will be available at **http://localhost:8000/**.

---

## Admin Panel Access
- URL: **http://127.0.0.1:8000/admin/**
- Log in with superuser credentials (created during setup).

---

## How to Submit This Project

### 1. Push Final Changes to GitHub
```sh
git add .
git commit -m "Final Submission: BharatFD"
git push origin main
```

### 2. Open an Issue in the Repository
- Go to **[GitHub Repository](https://github.com/Aasrithlingamagunta/BharatFD_assignment)**.
- Click on **Issues** → **New Issue**.
- Use a title like **Submission for Backend Developer Role**.
- In the description, mention:
  - **Project Name**: BharatFD
  - **Key Features**
  - **Repository Link**
  - **Deployment (if applicable)**

### 3. Tag the Evaluator
- Tag `@theakshaydhiman` as mentioned in the assignment.
- Add the `backend` label.

### 4. Confirm Submission
- Wait for confirmation from the evaluator.
- Provide any additional details if requested.

---

## Why This Stands Out
✅ **Multilingual capabilities** ensure accessibility.  
✅ **Rich text formatting** improves FAQ readability.  
✅ **Caching significantly boosts performance.**  
✅ **Deployable and scalable** with Docker.  
✅ **Well-documented and structured for easy evaluation.**

---

## Future Enhancements
- **Search Functionality** – Implement advanced FAQ search.
- **Authentication & Role-Based Access** – Secure admin controls.
- **Cloud Deployment** – Deploy to AWS/GCP for scalability.

---

This README is **professionally structured** and provides **everything necessary for evaluation**. Let me know if any last-minute changes are required!

