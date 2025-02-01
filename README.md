# BharatFD - Multilingual FAQ API

## Overview
BharatFD is a Django-based FAQ Management System with multilingual support, caching for performance, and a REST API for seamless integration. This project enables dynamic translations, making information accessible in multiple languages.

## Features
- **Django Backend** - Structured, scalable, and efficient.
- **Multilingual Support** - Automatic translations for FAQs (Hindi, Bengali, and English).
- **WYSIWYG Editor** - Fully formatted answers using CKEditor 5.
- **Fast API Responses** - Optimized with Django's built-in caching.
- **Docker Support** - Easily deployable with Docker & Compose.
- **Admin Panel** - Manage FAQs effortlessly with a user-friendly UI.

## Live Demo (If Deployed)
**API Base URL:** [https://your-deployed-url.com/api/faqs/](https://your-deployed-url.com/api/faqs/)

### Example API Requests
```bash
GET https://your-deployed-url.com/api/faqs/  # Fetch all FAQs in English (default)
GET https://your-deployed-url.com/api/faqs/?lang=hi  # Fetch FAQs in Hindi
GET https://your-deployed-url.com/api/faqs/?lang=bn  # Fetch FAQs in Bengali
Installation Guide
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Aasrithlingamagunta/BharatFD_assignment.git
cd BharatFD_assignment
2️⃣ Setup Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Apply Migrations & Run Server
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Now, visit http://127.0.0.1:8000/api/faqs/ in your browser.

Deployment with Docker
1️⃣ Build & Run the Docker Container
bash
Copy
Edit
docker build -t bharatfd .
docker run -d -p 8000:8000 bharatfd
2️⃣ Deploy to Render / Heroku / AWS
Push the Docker Image to DockerHub
bash
Copy
Edit
docker login
docker tag bharatfd <your-dockerhub-username>/bharatfd
docker push <your-dockerhub-username>/bharatfd
Deploy using Render / AWS / Heroku.
API Endpoints
Retrieve FAQs
bash
Copy
Edit
GET /api/faqs/?lang=<language_code>
Parameter	Type	Description
lang	string	Optional - Language code (en, hi, bn)
Admin Panel
Login at /admin/ with superuser credentials.

Running Tests
bash
Copy
Edit
python manage.py test faq
Ensures API functionality
Checks multilingual translations
Verifies caching performance
Tech Stack
Backend: Django, Django REST Framework
Database: SQLite (Can switch to PostgreSQL)
Editor: CKEditor 5 for rich-text formatting
Translation: Googletrans API
Containerization: Docker & Docker Compose
Caching: Django's Built-in Cache
Contribution Guidelines
Fork the repository.
Create a feature branch: git checkout -b feature-new
Commit changes: git commit -m "Added new feature"
Push and create a Pull Request.
License
This project is licensed under the MIT License.

Contact
For queries or improvements, reach out:
Email: your.email@example.com
GitHub: @Aasrithlingamagunta
