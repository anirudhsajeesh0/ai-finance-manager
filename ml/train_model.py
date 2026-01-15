import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ===== TRAINING DATA =====
texts = [
    # FOOD
    "pizza",
    "burger",
    "restaurant bill",
    "food delivery",
    "dinner",
    "lunch",
    "hotel food",

    # TRAVEL
    "uber ride",
    "ola cab",
    "bus ticket",
    "train ticket",
    "flight booking",
    "taxi fare",
    "travel expense",

    # SALARY
    "salary credited",
    "monthly salary",
    "company payroll",
    "income received",
    "bonus credited",

    # RENT
    "house rent",
    "room rent",
    "hostel fee",
    "pg rent",
    "flat rent",

    # SHOPPING
    "amazon purchase",
    "flipkart order",
    "clothes shopping",
    "online shopping",
    "mall purchase"
]

labels = [
    "Food","Food","Food","Food","Food","Food","Food",
    "Travel","Travel","Travel","Travel","Travel","Travel","Travel",
    "Salary","Salary","Salary","Salary","Salary",
    "Rent","Rent","Rent","Rent","Rent",
    "Shopping","Shopping","Shopping","Shopping","Shopping"
]

# ===== VECTORIZE =====
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# ===== TRAIN MODEL =====
model = MultinomialNB()
model.fit(X, labels)

# ===== SAVE MODEL =====
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model retrained successfully")
