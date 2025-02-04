# -*- coding: utf-8 -*-
import subprocess
import json
import os


def transcribe_audio_to_json(audio_path):
    whisper_path = "/opt/homebrew/bin/whisper"  # Whisper 安裝路徑
    ffmpeg_path = "/opt/homebrew/bin/ffmpeg"
    
    # 設定環境變數，確保 subprocess 找得到 ffmpeg
    env = os.environ.copy()
    env["PATH"] += os.pathsep + "/opt/homebrew/bin"

    # 執行 Whisper 命令行工具
    result = subprocess.run(
        [whisper_path, audio_path, "--model", "medium", "--output_format", "json"],
        capture_output=True,
        text=True,
        env=env  # 加入環境變數
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
