import yt_dlp
import os


def download(link, folder: str, name: str):
    # ydl_opts = {'outtmpl': name}
    # title, uploader, duration, view_count, like_count, resolution, ext
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(link, download=False)
        print(f"Title: {info['title']}")
        print(f"Author: {info['uploader']}")
        print(f"Duration: {info['duration']} sec.")
    author = list(info['uploader'].split())[0:2]
    ydl_opts = {
        'merge_output_format': 'mp4',
        'outtmpl': f"{folder}/{info['title']}_{' '.join(author)}.mp4",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


f = open("links.txt", 'r')
lines = f.readlines()
f.close()
n = len(lines)
index = 0
base_name = "video"
out_folder = "download"
os.makedirs(out_folder, exist_ok=True)  # Создаёт папку, если её нет
for i in range(n):
    s = lines[i].strip()
    download(s, out_folder, f"{base_name}_{i}")
