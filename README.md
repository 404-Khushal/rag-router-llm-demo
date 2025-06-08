# 🧠 RAG-Paper-Reader

A simple Retrieval-Augmented Generation (RAG) app that lets you **summarize and ask questions about research papers** using LlamaIndex and Groq LLMs. Built with **Streamlit** for the frontend.

## 📚 What it does

- Takes a research paper (PDF) as input
- Splits it into readable chunks (nodes)
- Builds two powerful tools:
  - 🔍 **Vector Tool** – Finds answers based on your questions
  - 🧾 **Summary Tool** – Gives structured summaries
- Uses **RouterLLM** to automatically decide which tool to use
- Lets you ask **natural questions** through a friendly web interface

---

## 🚀 Live Demo @ 


---

## 🧰 Tech Stack

- 🧠 [LlamaIndex](https://github.com/jerryjliu/llama_index) for RAG + routing
- ⚡ [Groq API](https://console.groq.com/) for blazing fast inference
- 🧠 HuggingFace Embeddings
- 🕸️ Streamlit for frontend
- 📄 Research papers (PDFs)

---

## 📝 Setup Instructions

### 1. Clone the repo

git clone https://github.com/yourusername/RAG-Paper-Reader.git
cd RAG-Paper-Reader

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your secrets
Create a .streamlit/secrets.toml file:
GROQ_API_KEY = "your-groq-api-key"

### 4. Add your PDF papers
Put your research papers inside a papers/ folder. Example:
papers/
├── Attention.pdf
├── BERT.pdf

### 5. Run the app
streamlit run app.py

## 📂 Project Structure
RAG-Paper-Reader/
├── app.py                  # Main Streamlit app
├── requirements.txt        # All dependencies
├── papers/                 # Research PDFs

##✅ Features
Supports multiple PDFs
Clean user interface
Smart routing between summary and vector tools
Easy to expand for other document types


