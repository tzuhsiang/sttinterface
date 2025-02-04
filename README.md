# sttinterface
上傳錄音檔，利用whisper音轉字模組，把音檔轉成文字檔，呈現在介面上。

### 上傳檔案介面與whisper轉譯結果
![網站介面](images/demo.png)

# 需求套件
- streamlit
- whisper
- 其他基本python套件
- docker(optional)
- docker-compose(optional)

# 執行指令(用本機環境)
streamlit run app.py

# 建置映像檔(optional)
docker compose build

# 啟動系統(optional)
docker compose up -d