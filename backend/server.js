const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// ================== IN-MEMORY DATA ==================
let transactions = [];
let idCounter = 1;

// ================== TEST ROUTE ==================
app.get("/", (req, res) => {
  res.send("Backend is running");
});

// ================== GET ALL TRANSACTIONS ==================
app.get("/transactions", (req, res) => {
  res.json(transactions);
});

// ================== ADD TRANSACTION ==================
app.post("/transactions", (req, res) => {
  const { desc, amount, category, type } = req.body;

  if (!desc || !amount || !type) {
    return res.status(400).json({ message: "Invalid data" });
  }

  const newTransaction = {
    id: idCounter++,
    desc,
    amount,
    category: category || "Other",
    type
  };

  transactions.push(newTransaction);
  res.status(201).json(newTransaction);
});

// ================== DELETE TRANSACTION ==================
app.delete("/transactions/:id", (req, res) => {
  const id = Number(req.params.id);
  transactions = transactions.filter(t => t.id !== id);
  res.json({ message: "Transaction deleted" });
});

// ================== START SERVER ==================
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

