# 🤖 Investor Relations Chatbot

An **AI-powered Investor Relations Chatbot** built with **Python & Flask** that answers company-related questions using document ingestion and retrieval. This project demonstrates practical skills in backend development, NLP workflows, and API design — suitable for **internship and entry-level roles**.

---

## 🚀 Features

* 📄 Ingests company documents (PDF/text)
* 🔍 Retrieves relevant context for user queries
* 🌐 REST API built with Flask
* 🧠 LLM-ready architecture (can plug Gemini / OpenAI)
* 🗂 Clean project structure

---

## 🛠 Tech Stack

* **Language:** Python 3
* **Backend:** Flask
* **Environment:** Virtualenv (.venv)
* **NLP:** Text chunking & embeddings (extensible)
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```
investor_chatbot/
├── ingest.py           # Document loading & processing
├── chatbot.py          # Core chatbot logic
├── chat.py             # API / CLI entry point
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored files (venv, cache)
└── README.md           # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/TarunKayat/investor-chatbot.git
cd investor-chatbot
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python chat.py
```

Example:

```
🤖 Investor Relations Chatbot
Type 'exit' to quit
```

---

## 🧪 Example Use Cases

* Ask annual revenue of a company
* Query financial highlights from reports
* Build multilingual investor assistants

---

## 🎯 Why This Project is Internship-Ready

* ✅ Uses real-world backend patterns
* ✅ Demonstrates Git & clean commits
* ✅ Modular & readable code
* ✅ Easily extendable with LLM APIs
* ✅ Shows understanding of document-based QA systems

---

## 🔮 Future Improvements

* Add vector database (FAISS)
* Add frontend UI
* Add authentication
* Deploy on cloud (Render / AWS)

---

## 👨‍💻 Author

**Tarun Kayat**
Aspiring AI/ML & Backend Developer

🔗 GitHub: [https://github.com/TarunKayat](https://github.com/TarunKayat)

---

⭐ If you find this project useful, please give it a star!
