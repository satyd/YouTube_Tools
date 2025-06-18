from pytube import YouTube


def download_video(link):
    yt = YouTube(
        link,
        use_oauth=False,
        allow_oauth_cache=True
    )
    stream = yt.streams.get_highest_resolution()
    # Скачиваем видео
    print(f"Скачивается: {yt.title}")
    stream.download(output_path="downloads")  # папка, куда сохранить
    print("Готово!")


# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # замените на нужное видео
video_url = "https://youtu.be/f-gi8k4IRh8?si=YL8_KSwDWRvn7IWK"  # замените на нужное видео
video_url2 = "https://youtu.be/t1ZxYv49KwA?si=oYdhtieN-Aj6G0dx"
video_url3 = "https://youtu.be/t1ZxYv49KwA?si=jyA5EsWvYgJwDWFY"

f = open("link.txt", 'r')
url = f.readline().strip().replace("\n", "")
f.close()
print(url)

download_video(video_url3)
# Создаем объект YouTube
