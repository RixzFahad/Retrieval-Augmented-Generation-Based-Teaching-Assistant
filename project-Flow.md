# 🎓 RAG-Based AI Teaching Assistant  
### (Retrieval-Augmented Generation Based Learning System)

## 📌 Project Overview

This project builds a **RAG-based AI Teaching Assistant** that can answer questions from course videos.

The system:
- Takes course videos (Python 100 Days – CodeWithHarry)
- Converts them into structured text
- Chunks the content with timestamps
- Converts text into vector embeddings
- Stores embeddings
- Retrieves relevant chunks
- Generates contextual answers using an LLM

This enables students to query course content and get precise, timestamp-aware responses.

---

# 🏗️ Project Flow Architecture

## 🔹 Step 1: Video to Text (Transcription)

### Goal:
Convert course videos into text transcripts.

### Process:
- Selected 10 videos from the Python 100 Days series.
- Downloaded videos locally.
- Installed **FFmpeg** and configured environment path.
- Verified FFmpeg installation using terminal.
- Converted `.mp4` videos into `.mp3` audio files.
- Used **OpenAI Whisper (large-v2)** for transcription.

### Automation:
Created a preprocessing pipeline using Python + FFmpeg:
- Dynamically extracted metadata from filenames
- Converted videos into structured MP3 audio files
- Prepared audio files for transcription

### Output:
Each video is converted into:
- Transcribed text
- Stored in structured JSON format

---

## 🔹 Step 2: Whisper Transcription

### Model Used:
- `Whisper large-v2`

### Observations:
- High accuracy
- High computational cost
- 12-minute video takes ~30+ minutes
- Requires strong system memory and GPU capacity

### Output JSON Format:
Each transcript contains:

```json
{
  "start": 0.00,
  "end": 12.45,
  "text": "Transcribed sentence..."
}
```

This stores:
- Start timestamp
- End timestamp
- Spoken text

---

## 🔹 Step 3: Chunking

### Goal:
Break large transcripts into manageable pieces for embedding.

Each chunk contains:
- `start`
- `end`
- `text`
- `video_number`

All chunks stored in structured JSON.

### Why Chunking?
- Improves retrieval accuracy
- Enables semantic search
- Reduces embedding noise
- Makes RAG pipeline efficient

### Result:
- 10 videos processed
- Total ~15,562 lines of chunked data

---

## 🔹 Step 4: Text to Vector (Embedding)

### Goal:
Convert text chunks into vector embeddings.

Process:
- Generate embeddings for each chunk
- Store embeddings in vector database

Each chunk becomes:

```
Text → Embedding → Stored Vector
```

This enables semantic similarity search.

---

## 🔹 Step 5: RAG Setup

RAG (Retrieval-Augmented Generation) Pipeline:

1. User asks a question
2. Question converted into embedding
3. Vector database retrieves most relevant chunks
4. Retrieved context sent to LLM
5. LLM generates contextual response

---

## 🔹 Step 6: Querying & Response Generation

When a student asks:

> "What is Python list comprehension?"

System:
- Searches vector database
- Finds relevant chunk with timestamp
- Sends context to LLM
- Returns:
  - Answer
  - Related video number
  - Exact timestamp

This allows students to:
- Learn faster
- Jump directly to video segment
- Avoid rewatching entire lecture

---

# 🛠️ Technologies Used

- Python
- OpenAI Whisper (large-v2)
- FFmpeg
- JSON
- Vector Embeddings
- RAG Architecture
- LLM for Response Generation

---

# ⚙️ Challenges Faced

- Large-v2 model is computationally expensive
- MP3 to text conversion takes significant time
- High memory usage
- Need proper chunk structuring
- Timestamp alignment accuracy

---

# 🚀 Final Output

The system now:

✔ Converts videos to text  
✔ Chunks transcripts with timestamps  
✔ Stores structured JSON data  
✔ Creates embeddings  
✔ Retrieves relevant knowledge  
✔ Generates intelligent answers  

Total processed:
- 10 videos
- 15,562+ chunk lines
- Fully structured metadata pipeline

---

# 🎯 Future Improvements

- Switch to faster Whisper model (medium/small for speed)
- Use GPU optimization fully
- Implement real-time query interface
- Deploy using Streamlit or FastAPI
- Add citation + clickable timestamps

---

# 🧠 Why This Project Matters

This project demonstrates:

- End-to-end AI data pipeline creation
- Automated lecture preprocessing
- Real-world RAG implementation
- Vector search system
- AI-powered educational assistant

It replicates modern AI assistant architecture used in industry systems.

---

## 👨‍💻 Author

Fahad Khan (Rixz)  
Data Analyst | AI Enthusiast | RAG Builder
