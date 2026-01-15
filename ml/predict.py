from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # allow React to access this API

# ===== LOAD MODEL & VECTORIZER =====
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ===== HEALTH CHECK ROUTE =====
@app.route("/")
def home():
    return "ML API is running"

# ===== PREDICTION ROUTE =====
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"category": "Other"})

    # Vectorize input
    X = vectorizer.transform([text])

    # Get prediction probabilities
    probs = model.predict_proba(X)[0]
    max_prob = np.max(probs)
    prediction = model.classes_[np.argmax(probs)]

    # Confidence threshold
    if max_prob < 0.25:
        prediction = "Other"

    return jsonify({
        "category": prediction,
        "confidence": round(float(max_prob), 2)
    })

# ===== RUN SERVER =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
