FROM python:3.11.6

COPY package.json /app/

WORKDIR /app

RUN pip3 install torch torchvision torchaudio
RUN pip install openai-whisper
RUN choco install ffmpeg 
RUN pip install pydub
RUN pip install pyAudioAnalysis
RUN pip install scipy
RUN pip install scikit-learn
RUN pip install hmmlearn
RUN pip install matplotlib
RUN pip install eyed3
RUN pip install imbalanced-learn
RUN pip install plotly
RUN pip install pyAudioDiarization



CMD ["main.py"]

