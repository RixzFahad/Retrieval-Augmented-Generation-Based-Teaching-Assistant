# 📚 RAG-Based AI Teaching Assistant

An end-to-end **Retrieval-Augmented Generation (RAG)** pipeline that converts video lectures into an intelligent AI assistant capable of answering context-aware questions.

This system transforms raw video content into structured knowledge using transcription, chunking, embeddings, and semantic retrieval — enabling grounded AI responses.

---

## 🚀 Project Overview

This project allows users to:

- Upload lecture videos (.mp4)
- Extract audio using FFmpeg
- Transcribe speech into text using Whisper
- Split transcripts into structured chunks
- Generate vector embeddings
- Store embeddings in a vector database
- Retrieve relevant content based on user queries
- Generate context-aware answers using an LLM

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an AI architecture that:

1. Retrieves relevant information from a knowledge base
2. Augments the user query with retrieved context
3. Generates accurate responses using a language model

This ensures answers are grounded in actual lecture content rather than relying only on the model’s pre-trained knowledge.

---

## 🏗️ System Architecture

Video Files (.mp4)
↓
Audio Extraction (FFmpeg)
↓
Speech-to-Text (Whisper)
↓
Text Cleaning & Chunking
↓
Embedding Generation
↓
Vector Database Storage
↓
User Query
↓
Similarity Search (Top-K Retrieval)
↓
LLM Response Generation

---

## ⚙️ Tech Stack

- Python
- OpenAI Whisper (Speech-to-Text)
- FFmpeg (Audio Extraction)
- Embedding Model
- Vector Database (FAISS / ChromaDB)
- LLM API (Response Generation)

---

## 📂 Project Structure

RAG-Based-AI-Teaching-Assistant/
│
├── videos/ # Input lecture videos
├── audio/ # Extracted MP3 files
├── transcripts/ # Generated text transcripts
├── embeddings/ # Stored vector embeddings
├── rag_pipeline.py # Main pipeline script
├── requirements.txt
└── README.md

---

## 🔄 Workflow

### 1️⃣ Video to Audio

Extract audio from lecture videos using FFmpeg.

### 2️⃣ Audio to Text

Transcribe audio files into text using Whisper.

### 3️⃣ Text Chunking

Split transcripts into smaller context-aware chunks.

### 4️⃣ Embedding Creation

Convert text chunks into vector embeddings.

### 5️⃣ Vector Storage

Store embeddings inside a vector database for semantic search.

### 6️⃣ Query Processing

- Convert user query into embedding
- Retrieve top-k similar chunks
- Pass retrieved chunks + query to LLM
- Generate grounded response

---

## 🎯 Key Features

✔ End-to-end automated pipeline  
✔ Handles large lecture datasets  
✔ Semantic similarity-based retrieval  
✔ Context-aware AI-generated responses  
✔ Modular and reusable architecture

---

## 💡 Example Use Case

User Question:
"What is the difference between supervised and unsupervised learning?"

System Process:

- Retrieves relevant lecture chunks
- Augments query with retrieved context
- Generates an accurate, course-grounded answer

---

## 🧪 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python rag_pipeline.py
```

---

## 📈 Future Improvements

- Add Streamlit or React frontend
- Add multi-language transcription support
- Implement hybrid search (keyword + semantic)
- Deploy on cloud (AWS/GCP/Azure)
- Add conversational memory

---

## 👨‍💻 Author
Mentor - @CodeWithHarry - Harish ALi Khan
Fahad Khan (Rixz)  
Aspiring Data Scientist | AI Engineer | Data Analsyt
Building practical AI systems with real-world applications.
