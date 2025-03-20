from pytube import YouTube

url = YouTube("https://www.youtube.com/watch?v=g8dmQs2Fzns")

video = url.streams.filter(only_audio = True).first()

video.download(f".\\", filename = "temp.mp3")