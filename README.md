# AI-Powered Personal Finance Manager 💰🤖

An AI-powered personal finance management system that automatically categorizes income and expenses using Machine Learning.  
The system provides real-time AI suggestions while the user types, along with financial summaries and visualizations.

---

## 🚀 Features

- Add income and expense transactions
- Real-time AI-based expense categorization
- Machine Learning model trained using text data
- React frontend with interactive UI
- Flask-based ML inference API
- Category-wise and income vs expense analysis
- Scalable full-stack architecture

---

## 🧠 How the AI Works

- Transaction descriptions are sent to a **Flask ML API**
- A **TF-IDF + Logistic Regression** model predicts the category
- A confidence threshold avoids incorrect predictions
- The model can be retrained with new data for better accuracy

---

## 🛠 Tech Stack

### Frontend
- React.js
- JavaScript, HTML, CSS
- Chart.js

### Backend / ML
- Python
- Flask
- Scikit-learn
- Flask-CORS

---

## 📁 Project Structure
ai-finance-manager/
│
├── frontend/ # React frontend
│ ├── src/
│ ├── package.json
│
├── ml/ # Machine Learning & Flask API
│ ├── train_model.py
│ ├── predict.py
│ ├── model.pkl
│ ├── vectorizer.pkl
│
├── README.md
└── .gitignore


---

## ⚙️ How to Run the Project (Step-by-Step)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-finance-manager.git
cd ai-finance-manager

cd ml
pip install flask flask-cors scikit-learn numpy
pip install flask flask-cors scikit-learn numpy
python train_model.py
python predict.py
http://127.0.0.1:8000
Keep this terminal running.

3️⃣ Run the Frontend (React)

Open a new terminal, then:

cd frontend
npm install
npm start


React app will open at:

http://localhost:3000

🧪 Example Usage

Type pizza → AI Suggestion: Food

Type uber ride → AI Suggestion: Travel

Type salary credited → AI Suggestion: Salary

Type random text → AI Suggestion: Other

📄 License

This project is intended for educational and academic use.


