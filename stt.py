import whisper
import json

# Load Whisper model
model = whisper.load_model("large-v2")

# Transcribe / Translate
result = model.transcribe(
    audio="audio/1_Day1.mp3",
    language="hi",
    task="translate",
    word_timestamps=False
)

# Print full segments (with timestamps)
print(result["segments"])

# Create chunks list
chunks = []

for segment in result["segments"]:
    chunks.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    })

# Print chunks
print(chunks)

# Save to JSON file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4, ensure_ascii=False)

print("✅ Output saved to output.json")