import whisper as whisper_OG
import whisper_timestamped as whisper
import json
#code ausschnitt geliehen von https://github.com/linto-ai/whisper-timestamped?tab=readme-ov-file#installation
audio = whisper.load_audio("podcast/knowledge_science_ep1.mp3")

model = whisper.load_model("base", device="cpu")

result = whisper.transcribe(model, audio)

with open("transcription.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(result, indent=2, ensure_ascii=False))
print("done")