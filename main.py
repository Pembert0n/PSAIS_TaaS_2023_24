import whisper as whisper_OG
import whisper_timestamped as whisper
import json
#code ausschnitt geliehen von https://github.com/linto-ai/whisper-timestamped?tab=readme-ov-file#installation
audio = whisper.load_audio("podcast/knowledge_science_ep1.mp3")

model = whisper.load_model("tiny", device="cpu")

result = whisper.transcribe(model, audio, language="de")


print(json.dumps(result, indent = 2, ensure_ascii = False))


# model = whisper.load_model("base")
# result = model.transcribe("podcast/knowledge_science_ep1.mp3")

# with open("transcription.txt", "w") as f:
#     f.write(result["text"])
# print("done")