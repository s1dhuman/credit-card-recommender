# Credit Card Recommendation System

A modern, AI-powered web application that recommends the best credit cards to users based on their profile and preferences.

## 🚀 Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React (Vite)
- **Database:** PostgreSQL (planned)
- **AI Integration:** LangChain + OpenAI (planned)
- **Testing:** Postman, Swagger UI

## 📁 Project Structure
project-root/
├── backend/
│ ├── main.py
│ └── app/
│ ├── routes/
│ ├── models/
│ └── schemas/
├── frontend/
├── .gitignore
└── README.md

 
## 💡 Features
- [x] FastAPI backend with modular structure
- [x] User profile schema for recommendations
- [x] Dummy credit card recommendation endpoint
- [x] API documentation via Swagger UI
- [ ] PostgreSQL integration for persistent storage
- [ ] AI-powered recommendations (LangChain + OpenAI)
- [ ] React frontend with chat interface

## 🛠️ Getting Started

### Clone the Repository
git clone https://github.com/s1dhuman/credit-card-recommender.git
cd credit-card-recommender


### Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate # On Windows
pip install -r requirements.txt
uvicorn main:app --reload

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for API docs.

## 🧪 Testing the API
- Use Swagger UI at `/docs` or Postman to test endpoints.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 📄 License
This project is licensed under the MIT License.
