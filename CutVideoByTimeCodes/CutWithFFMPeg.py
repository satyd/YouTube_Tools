import subprocess
import re
import os
from CutVideoByTimecodes import *

out_folder = "output"


def cut_with_ffmpeg(video_path, start, end, output_path):
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-ss", str(start),
        *(["-to", str(end)] if end is not None else []),  # Добавляем "-to" только если end не None
        "-c:v", "libx264",
        "-c:a", "aac",
        "-avoid_negative_ts", "make_zero",
        "-movflags", "+faststart",
        output_path
    ]
    subprocess.run(cmd)


os.makedirs(out_folder, exist_ok=True)  # Создаёт папку, если её нет
# Пример вызова:
timecodes = parse_timecodes("timecodes.txt")
print(*timecodes)
for t in timecodes:
    cut_with_ffmpeg("video.webm", t[0], t[1], f"{out_folder}/{t[2]}.mp4")
