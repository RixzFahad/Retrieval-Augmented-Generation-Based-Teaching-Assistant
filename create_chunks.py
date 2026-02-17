import whisper
import json
import os
import torch

AUDIO_DIR = "audio"          # change to "audio" if your folder name is audio
OUT_FILE = "output.json"

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

model = whisper.load_model("medium").to(device)

# ✅ Only mp3 files
audios = [f for f in os.listdir(AUDIO_DIR) if f.lower().endswith(".mp3")]
audios.sort()

all_results = []

for audio in audios:
    file_path = os.path.join(AUDIO_DIR, audio)

    # ✅ Extract number + title safely
    name_no_ext = os.path.splitext(audio)[0]  # "1_Day1"
    if "_" in name_no_ext:
        number, title = name_no_ext.split("_", 1)
    else:
        number, title = "", name_no_ext

    print("Processing:", number, title)

    # ✅ Transcribe
    result = model.transcribe(
        audio=file_path,
        language="hi",
        task="translate",
        word_timestamps=False
    )

    # ✅ Segments -> chunks
    chunks = [
        {
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        }
        for seg in result.get("segments", [])
    ]

    all_results.append({
        "file": audio,
        "number": number,
        "title": title,
        "chunks": chunks,
        "full_text": result.get("text", "").strip()
    })

# ✅ Save ONCE (no overwrite)
with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f"✅ Processing completed! Saved: {OUT_FILE} | files: {len(all_results)}")