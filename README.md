# 📚 BookSuggest - Book Recommendation System

BookSuggest is a web-based Book Recommendation System built using Flask. It offers personalized book suggestions and showcases the top 50 books based on ratings and popularity. The project utilizes collaborative filtering and content-based filtering using a precomputed similarity matrix.

---

## 🚀 Features

- 🔍 Search any book and get 5 similar recommendations
- 📈 View top 50 popular books with:
  - Title
  - Author
  - Ratings
  - Number of Votes
  - Book Cover Image
- 🎨 Dark-themed Bootstrap 5 responsive interface
- 🧠 ML Model using cosine similarity for recommendations

---

## 🛠️ Tech Stack

- **Backend:** Flask, Python
- **Frontend:** HTML, CSS, Bootstrap 5
- **Data Processing:** Pandas, NumPy
- **Model:** Content-Based Filtering using Cosine Similarity
- **Deployment-ready:** Vercel / Render compatible

---


## 📁 Project Structure
BookSuggest/
│
├── static/
│ └── style.css # Custom CSS styles
│
├── templates/
│ ├── index.html # Homepage with top 50 books and search bar
│ └── recommend.html # Recommendation result page
│
├── .gitignore # Git ignored files
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── runtime.txt # Python version for deployment
│
├── popular.pkl # Pickled DataFrame of top 50 books
├── pt.pkl # Pickled pivot table
├── books.pkl # Pickled DataFrame with book metadata
├── similarity_score.pkl # Cosine similarity matrix
│
└── README.md # Project documentation (this file)


---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Nishant8704/BookSuggest.git
cd BookSuggest

python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows

pip install -r requirements.txt

python app.py

# 👨‍💻 Author

## Nishant Raj

- 🎓 Computer Science & Engineering (AI/ML) @ Chandigarh University
- 💼 Aspiring Data Scientist & ML Developer
- 📚 Passionate about Recommender Systems, AI Projects, and Full-Stack Development
- 🤖 Active contributor in Robo Club and tech communities

### 🌐 Connect with Me

- GitHub: [github.com/Nishant8704](https://github.com/Nishant8704)
- LinkedIn: [linkedin.com/in/nishant-raj04](https://linkedin.com/in/nishant-raj04)
Apache License

Copyright (c) 2025 Nishant Raj

