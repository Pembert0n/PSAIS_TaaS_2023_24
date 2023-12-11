import json
import glob
import os
import whisper as whisper_OG
import whisper_timestamped as whisper

file_pattern = "podcast/knowledge_science_ep*.mp3"
output_folder = "transcriptions/"

model = whisper.load_model("base", device="cpu")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = glob.glob(file_pattern)

for file_path in files:
    audio = whisper.load_audio(file_path)
    
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    result = whisper.transcribe(model, audio)
    
    output_file = os.path.join(output_folder, f"{file_name}_transcription.txt")
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"Transkription für {file_name} abgeschlossen.")

print("Alle Transkriptionen abgeschlossen.")
