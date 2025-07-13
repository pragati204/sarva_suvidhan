
# 🎥 Video Script: KPA API Assignment

## 👋 Introduction
Hello, my name is [Your Name]. This is a short demo of the KPA backend API assignment. I have implemented two APIs using FastAPI and PostgreSQL.

## ⚙️ Tech Stack
- Python with FastAPI
- PostgreSQL as the database
- SQLAlchemy ORM
- Postman for testing

## 🚀 APIs Implemented

### 1. `POST /user/login`
- Accepts phone and password
- Checks against database records
- Returns success or error response

### 2. `GET /form/all`
- Retrieves a list of form entries from the database

## 🧪 Testing with Postman
- [Show Postman interface]
- Test login with credentials: 7760873976 / to_share@123
- Test form list API and show the JSON response

## 📁 Project Structure
- `main.py`: Initializes the FastAPI app
- `models.py`: Contains SQLAlchemy models
- `routes/`: Contains API route logic
- `.env`: Holds DB configuration

## 📦 Final Notes
- I’ve added basic input validation
- DB setup and test data included
- Thank you for reviewing my submission!
