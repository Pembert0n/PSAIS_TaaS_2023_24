from pydub import AudioSegment

# Lade das Whisper-Modell und führe die Transkription durch
import whisper
model = whisper.load_model("base")
result = model.transcribe("podcast/knowledge_science_ep1.mp3")
transcription_text = result["text"]

# Lade die Audiodatei
audio_file = "podcast/knowledge_science_ep1.mp3"  # Passe den Pfad zur Audiodatei an
audio = AudioSegment.from_file(audio_file)

# Erzeuge eine Instanz der Sprecherdiarization
diarization = SpeakerDiarization()

# Führe die Sprechererkennung durch
results = diarization.detect_speakers(audio_file)

# Erhalte die Sprecherwechsel und die dazugehörigen Zeitstempel
speaker_changes = results['speaker_changes']

# Erstelle Zeitstempel pro Sprecherwechsel
timestamps = []
for i in range(len(speaker_changes) - 1):
    start_time = speaker_changes[i]
    end_time = speaker_changes[i + 1]
    sentence = transcription_text[start_time:end_time]
    timestamps.append(f"{start_time/1000:.2f} - {end_time/1000:.2f}: {sentence}")

# Speichere die Transkription mit Zeitstempeln pro Sprecherwechsel in einer Datei
with open("transcription_with_speaker_timestamps.txt", "w") as f:
    for timestamp in timestamps:
        f.write(timestamp + "\n")

print("done")