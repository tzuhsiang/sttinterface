# -*- coding: utf-8 -*-
import subprocess
import json
import os
import shutil

def transcribe_audio_to_json(audio_path):
    # 嘗試自動找到 Whisper 執行檔
    whisper_path = shutil.which("whisper")

    if whisper_path is None:
        raise FileNotFoundError("找不到 Whisper 執行檔，請確認 Whisper 是否已正確安裝在 Docker 容器內")

    # 執行 Whisper 命令行工具
    result = subprocess.run(
        [whisper_path, audio_path, "--model", "medium", "--output_format", "json"],
        capture_output=True,
        text=True
    )

    content = result.stdout.split("\n")

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
    
    print("Transcription saved data.json")
    
    return result.stdout

# 範例使用
if __name__ == "__main__":
    audio_file = "uploads/howtobehappy.m4a"
    transcribe_audio_to_json(audio_file)
