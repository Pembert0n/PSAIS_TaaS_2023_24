import whisper

model = whisper.load_model("base")
result = model.transcribe("podcast/knowledge_science_ep1.mp3")

with open("transcription.txt", "w") as f:
    f.write(result["text"])
print("done")