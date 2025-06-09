#  RAG Paper Reader

A simple and effective **Retrieval-Augmented Generation (RAG)** app that lets you **summarize and ask questions** about research papers using **LlamaIndex**, **Groq**, and **Streamlit**.

---

## 📚 What It Does

- Accepts research papers (PDFs) as input
- Splits them into readable chunks (nodes)
- Builds two smart tools:
  - 🔍 **Vector Tool** – Finds answers from specific parts of the paper
  - 🧾 **Summary Tool** – Summarizes the paper in a structured format
- Uses **RouterLLM** to automatically select the right tool for your question
- Clean and minimal **Streamlit** interface for interaction

---

## 🚀 Live Demo

https://rag-router-llm-demo-bnmweuahuwskepbfjxkyhg.streamlit.app/

---

## 🧰 Tech Stack

- 🧠 [LlamaIndex](https://github.com/jerryjliu/llama_index) – core RAG framework
- ⚡ [Groq API](https://console.groq.com/) – superfast LLM backend
- 💬 HuggingFace Embeddings – to vectorize text
- 🖥️ Streamlit – for building the web UI
- 📄 PDF documents as source material

---

## 📝 Setup Instructions

### 1. Clone the Repository
git clone https://github.com/yourusername/RAG-Paper-Reader.git
cd RAG-Paper-Reader

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Add Your API Key
Create a file at `.streamlit/secrets.toml`:
GROQ_API_KEY = "your-groq-api-key"

### 4. Add Research Papers
Place your PDF files in a folder named `papers/`, like this:
papers/
├── Attention.pdf
├── BERT.pdf

### 5. Run the App
streamlit run app.py

---

## 📂 Project Structure

RAG-Paper-Reader/
├── app.py                  # Streamlit app
├── requirements.txt        # Python dependencies
├── papers/                 # PDF research papers

---

## ✅ Features

* 💡 Clean, user-friendly interface
* 🧠 Smart summary and vector-based question answering
* 🔄 Easy to customize for different documents or models

---

## 🙌 Contributions

Pull requests and forks are welcome! Let’s build better research tools together.

---
