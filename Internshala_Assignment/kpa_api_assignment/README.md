# KPA Backend API Assignment

## 🔧 Setup Instructions

1. Clone the repo or unzip the code
2. Create virtual environment & activate it
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Set DB credentials in `.env` file
5. Create DB tables
   ```bash
   uvicorn app.main:app --reload
   ```

## ✅ APIs Implemented

1. `POST /user/login`  
   - Input: phone, password  
   - Output: success or error response  

2. `GET /form/all`  
   - Returns a list of all forms

## 🛠️ Tech Stack
- Python (FastAPI)
- PostgreSQL
- SQLAlchemy

## 📌 Assumptions
- User and Form data are pre-inserted manually for testing.
- No authentication token logic is implemented (only login match check).

## 📁 Postman Collection
Import `kpa_postman_collection.json` and test:
- `POST /user/login`
- `GET /form/all`

## 📽️ Demo Video
📎 [project-features]: https://drive.google.com/your_video_1  
📎 [project-technical]: https://drive.google.com/your_video_2
