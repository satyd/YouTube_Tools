import yt_dlp


def download(link, name: str):
    # ydl_opts = {'outtmpl': name}
    # title, uploader, duration, view_count, like_count, resolution, ext
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(link, download=False)
        print(f"Title: {info['title']}")
        print(f"Author: {info['uploader']}")
        print(f"Duration: {info['duration']} sec.")
    author = list(info['uploader'].split())[0:2]
    ydl_opts = {
        'outtmpl': f"{info['title']}--{' '.join(author)}",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


f = open("links.txt", 'r')
lines = f.readlines()
f.close()
n = len(lines)
index = 0
base_name = "video"
for i in range(n):
    s = lines[i].strip()
    download(s, f"{base_name}_{i}")
