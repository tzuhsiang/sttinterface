### Dockerfile
FROM python:3.11

WORKDIR /app

COPY . /app

# 安裝必要的系統依賴（Whisper 需要 ffmpeg）
RUN apt-get update && apt-get install -y ffmpeg

# 確保 pip 是最新版本
RUN pip install --upgrade pip

# 使用快取加速 pip 安裝
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt && \
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip install openai-whisper

# 確保 whisper CLI 可用
RUN ln -s $(which whisper) /usr/local/bin/whisper


# 確保 stt 模組可用
COPY stt/stt.py /app/stt/stt.py

ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS false

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
