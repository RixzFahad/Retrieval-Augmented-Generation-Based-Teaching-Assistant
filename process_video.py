import whisper
import json
import os
import torch

AUDIO_DIR = "audio"
CHUNK_DIR = "chunks"

# Create chunks folder if not exists
os.makedirs(CHUNK_DIR, exist_ok=True)

# ✅ Detect device (GPU or CPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# ✅ Load model ONCE and move to device
model = whisper.load_model("medium")
model = model.to(device)

# Get mp3 files only
audios = [f for f in os.listdir(AUDIO_DIR) if f.lower().endswith(".mp3")]
audios.sort()

for audio in audios:
    file_path = os.path.join(AUDIO_DIR, audio)

    name_no_ext = os.path.splitext(audio)[0]

    if "_" in name_no_ext:
        number, title = name_no_ext.split("_", 1)
    else:
        number, title = "", name_no_ext

    print("Processing:", audio)

    result = model.transcribe(
        audio=file_path,
        language="hi",
        task="translate",
        word_timestamps=False,
        fp16=True if device == "cuda" else False  # ✅ GPU optimization
    )

    chunks = []
    for segment in result["segments"]:
        chunks.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })

    # Save each file separately inside chunks folder
    output_path = os.path.join(CHUNK_DIR, f"{name_no_ext}.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print("Saved:", output_path)

print("✅ All files processed successfully!")
