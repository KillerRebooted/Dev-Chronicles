from time import sleep

Sentence = "According to the News, You have been SUS lately"

x = 0

while x != len(Sentence):
    x += 1
    print(f"BREAKING NEWS: {Sentence[-x:]}", end="\r")
    sleep(0.1)

print(f"BREAKING NEWS: {Sentence}")