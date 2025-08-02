from moviepy import VideoFileClip
import re
import os

out_folder = "output_2"


def time_to_seconds(time_str):
    """Конвертирует время формата MM:SS в секунды."""
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds


def parse_timecodes(file_path):
    """Читает файл с таймкодами и возвращает список кортежей (start_time, end_time, name)."""
    with open(file_path, 'r',  encoding='utf-8') as file:
        lines = file.readlines()

    timecodes = []
    for i in range(len(lines)):
        # Ищем время и название (формат "0:00 - Intro")
        match = re.match(r'(\d+:\d+)\s*-\s*(.+)', lines[i].strip())
        if not match:
            continue

        start_time = time_to_seconds(match.group(1))
        name = match.group(2).strip()

        # Берём конец отрезка из следующей строки или конец видео
        if i < len(lines) - 1:
            next_match = re.match(r'(\d+:\d+)', lines[i + 1])
            end_time = start_time + 12  # time_to_seconds(next_match.group(1)) if next_match else None
        else:
            end_time = start_time + 15  # Последний отрезок идёт до конца видео

        timecodes.append((start_time, end_time, name))

    return timecodes


def cut_video_by_timecodes(video_path, timecodes):
    """Нарезает видео по таймкодам."""
    video = VideoFileClip(video_path)

    for i, (start, end, name) in enumerate(timecodes):
        # Если end == None, берём до конца видео
        subclip = video.subclipped(start, end) if end else video.subclipped(start)
        output_path = f"{out_folder}/{name}.mp4"
        subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Сохранено: {output_path}")


os.makedirs(out_folder, exist_ok=True)  # Создаёт папку, если её нет
# Пример использования
video_name = 'videoplayback.mp4'
timecodes = parse_timecodes("timecodes_2.txt")
cut_video_by_timecodes(video_name, timecodes)
