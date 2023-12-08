import whisper as whisper_OG
import whisper_timestamped as whisper
import json
import glob
import os

# Muster für die Dateinamen der Podcast-Folgen
file_pattern = "podcast/knowledge_science_ep*.mp3"
output_folder = "transcriptions/"

# Laden des Modells außerhalb der Schleife, wenn es für alle Folgen gleich bleibt
model = whisper.load_model("base", device="cpu")

# Überprüfen und Erstellen des Ordners für die Transkriptionsdateien, falls er nicht vorhanden ist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Durchsuchen nach allen passenden Dateien im Ordner
files = glob.glob(file_pattern)

for file_path in files:
    # Laden der Audio-Datei
    audio = whisper.load_audio(file_path)
    
    # Extrahieren des Dateinamens ohne den Pfad und die Dateierweiterung
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Transkription für jede Datei durchführen
    result = whisper.transcribe(model, audio)
    
    # Schreiben der Transkription in eine Datei mit dem entsprechenden Dateinamen
    output_file = os.path.join(output_folder, f"{file_name}_transcription.txt")
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"Transkription für {file_name} abgeschlossen.")

print("Alle Transkriptionen abgeschlossen.")
