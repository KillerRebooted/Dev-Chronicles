import subprocess
import sys
import os

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gTTS', 'pyttsx3', 'playsound'])

import gtts
from playsound import playsound

speech = gtts.gTTS("Never Gonna Give You Up, Never Gonna Let You Down", lang = "en", tld = "com")

speech.save("Speech.mp3")
playsound("Speech.mp3")

os.remove("Speech.mp3")