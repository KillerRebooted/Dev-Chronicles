import os, shutil, gtts, playsound
from time import sleep
from os import system

#pip install playsound==1.2.2
#Lower the Number at Line 54 (0.325) to Make the Dictating Faster and Increase the Number to Slow it down.

clear = lambda: system("cls")

clear()

print("NOTE: .txt Files ONLY!")
print()

text = input("Enter the File Name (without .txt): ")

num = 0

with open(f"{__file__.removesuffix('Text to Speech for HW.py')}" + text + ".txt", "r", encoding="utf8") as file:
    
    text = file.read()

try:    
    
    os.mkdir(f"{__file__.removesuffix('Text to Speech for HW.py')}Text to Speech for HW")

except:

    print("", end="\r")

finally:

    clear()

    x = 0

    for i in text.split():

        x += len(i)+1
        
        clear()
        print(text[:x])

        if i.lower().islower() == False:

            continue

        speech = gtts.gTTS(i, lang = "en", tld = "co.in", slow = False)

        speech.save(f"{__file__.removesuffix('Text to Speech for HW.py')}Text to Speech for HW\{num}.mp3")

        playsound.playsound(f"{__file__.removesuffix('Text to Speech for HW.py')}Text to Speech for HW\{num}.mp3")

        sleep(len(i) * 0.295)

        num += 1

shutil.rmtree(f"{__file__.removesuffix('Text to Speech for HW.py')}Text to Speech for HW")
