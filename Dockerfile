FROM python:3.11.6

COPY package.json /app/
COPY main2.py /app/
COPY podcast/* /app/podcast/
COPY docker-compose.yml /app/
COPY milvus_db.py /app/

WORKDIR /app

RUN pip3 install torch torchvision torchaudio
RUN pip install openai-whisper
RUN pip3 install whisper-timestamped
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y ffmpeg
RUN pip install pydub
RUN pip install pyAudioAnalysis
RUN pip install scipy
RUN pip install scikit-learn
RUN pip install hmmlearn
RUN pip install matplotlib
RUN pip install eyed3
RUN pip install imbalanced-learn
RUN pip install plotly
RUN pip install pyAudioAnalysis
RUN pip install pymilvus



CMD ["python", "main2.py"]


