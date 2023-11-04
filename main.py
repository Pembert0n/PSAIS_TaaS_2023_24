import whisper
print("alive1")
model = whisper.load_model("base")
print("alive2")
result = model.transcribe("podcast/knowledge_science_ep1.mp3")
print("alive3")
with open("transcription.txt", "w") as f:
    print("alive4")
    f.write(result["text"])
print("done")