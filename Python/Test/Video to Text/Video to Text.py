import base64, os

loc = __file__.removesuffix(os.path.basename(__file__))

with open(f"{loc}\\test_video.mp4", "rb") as videoFile:
    text = base64.b64encode(videoFile.read())
    #print(text)
    file = open(f"{loc}\\test_text.txt", "wb") 
    file.write(text)
    file.close()

    fh = open(f"{loc}new_video.mp4", "wb")
    fh.write(base64.b64decode(text))
    fh.close()