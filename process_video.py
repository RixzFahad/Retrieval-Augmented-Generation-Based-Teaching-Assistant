import os
import subprocess

video_folder = "videos"
output_folder = "audio"

os.makedirs(output_folder, exist_ok=True)

files = os.listdir(video_folder)

for file in files:
    if file.endswith(".mp4"):
        tutorial_number = file.replace("Day", "").replace(".mp4", "")
        file_name = file.replace(".mp4", "")

        input_path = os.path.join(video_folder, file)
        output_path = os.path.join(output_folder, f"{tutorial_number}_{file_name}.mp3")

        print(f"Converting {file} → {output_path}")

        subprocess.run([
            "ffmpeg",
            "-i", input_path,
            "-q:a", "0",
            "-map", "a",
            output_path
        ])

print("✅ All videos converted successfully!")