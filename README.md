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

```bash
git clone https://github.com/yourusername/RAG-Paper-Reader.git
cd RAG-Paper-Reader
