from pvrecorder import PvRecorder
import wave, struct 
import os
import pyautogui
 
loc = os.path.dirname(os.path.realpath(__file__))

for index, device in enumerate(PvRecorder.get_available_devices()):
    print(f"[{index}] {device}")
 
recorder = PvRecorder(device_index=0, frame_length=512) #(32 milliseconds of 16 kHz audio)
audio = []
path = f'{loc}\\aud.mp3'

try:
    recorder.start()

    while True:
        frame = recorder.read()
        audio.extend(frame)
except KeyboardInterrupt:
    recorder.stop()
    with wave.open(path, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio), *audio))
finally:
    recorder.delete()

import whisper

model = whisper.load_model("base")
result = model.transcribe(f"{loc}\\aud.mp3")

print(result["text"])

marks = []

for num in result["text"].split(","):
    new_num = ""
    for char in num:
        if char.isdigit():
            new_num += char
    if new_num:
        marks.append(int(new_num))


print(marks)

os.remove(f"{loc}\\aud.mp3")