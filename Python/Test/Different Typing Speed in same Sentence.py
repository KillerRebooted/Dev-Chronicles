from time import sleep

def LbL(Sentence, Time):

    x = len(Sentence)
    Loop = -1

    while x!=0:
        Loop += 1
        print(Sentence[Loop], end = "", flush=True)
        sleep(Time)
        x -= 1

    return ""

print()
print("Well", end="", flush=True)
sleep(1)
print(LbL(", I guess You are not the Talking Type", 0.1), end="", flush = True)
sleep(0.4)
LbL("...", 0.4)