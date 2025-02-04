import streamlit as st
import os
import pandas as pd
from PIL import Image
import PyPDF2
from stt.stt import transcribe_audio_to_json

# 設定頁面標題
st.set_page_config(page_title="拖拉式檔案上傳")

# 使用 CSS 調整頁面寬度
st.markdown("""
    <style>
        /* 調整頁面整體內容的最大寬度 */
        .block-container {
            max-width: 90% !important;  /* 設定寬度為 90% */
            padding-left: 5% !important;
            padding-right: 5% !important;
        }
    </style>
""", unsafe_allow_html=True)


# 建立上傳資料夾
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("📂 拖拉式檔案上傳")
st.write("請拖曳或選擇要上傳的檔案。")


# 創建左右兩個欄位
col1, col2 = st.columns([1, 2])

# 在左側欄位放置檔案上傳元件
with col1:
    uploaded_files = st.file_uploader("選擇檔案", type=["mp3", "wav", "m4a", "csv", "txt", "xlsx", "png", "jpg", "jpeg", "pdf"], accept_multiple_files=True)

# 在右側欄位顯示上傳的檔案內容
with col2:
    if uploaded_files:
        st.write("### 已上傳檔案:")
        for uploaded_file in uploaded_files:
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success(f"✅ {uploaded_file.name} 已成功上傳！")
            st.write(f"**檔案大小:** {uploaded_file.size / 1024:.2f} KB")

            # 如果是 CSV 或 Excel 顯示內容
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
                st.write("📊 預覽 CSV 內容:")
                st.dataframe(df)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
                st.write("📊 預覽 Excel 內容:")
                st.dataframe(df)
            elif uploaded_file.name.endswith((".png", ".jpg", ".jpeg")):
                image = Image.open(uploaded_file)
                st.image(image, caption=uploaded_file.name, use_container_width=True)
            elif uploaded_file.name.endswith(".pdf"):
                st.write("📄 PDF 預覽:")
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                for page_num in range(min(3, len(pdf_reader.pages))):  # 預覽最多3頁
                    page = pdf_reader.pages[page_num]
                    st.text(page.extract_text())
            elif uploaded_file.name.endswith(".txt"):
                st.write("📜 文本文件內容:")
                content = uploaded_file.read().decode("utf-8")
                st.text_area("內容", content, height=400)
            elif uploaded_file.name.endswith((".mp3", ".wav", ".m4a")):
                st.write("🎙️ 音訊轉文字中...")
                import time
                start_time = time.time()
                content = transcribe_audio_to_json(file_path)
                processing_time = time.time() - start_time
                st.write("📝 轉錄內容:")
                st.text_area("轉錄結果", content, height=200)
                st.write(f"⏱️ 處理時間: {processing_time:.2f} 秒")

st.write("---")
st.write("📥 上傳的檔案將存入 `uploads` 資料夾。")
