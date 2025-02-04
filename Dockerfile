### Dockerfile
FROM python:3.13

# 設定工作目錄
WORKDIR /app

# 複製當前目錄下的所有檔案到容器內
COPY . /app

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir openai-whisper

# 設定環境變數以避免 Streamlit 請求輸入
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS false

# 開放 Streamlit 端口
EXPOSE 8501

# 執行 Streamlit 應用
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
