FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install torch pandas numpy tensorflow seaborn matplotlib \
    beautifulsoup4 nltk bert-for-tf2 sentencepiece googletrans==4.0.0-rc1 tensorflow-hub

WORKDIR /app
COPY . /app

CMD ["python3"]
