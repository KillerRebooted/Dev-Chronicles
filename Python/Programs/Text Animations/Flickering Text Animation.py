import random, time

def animate_text(text, speed):

    printed_text = [""]*len(text)
    index = 0

    iter = 0

    while "".join(printed_text) != text:

        if iter != speed:
            choice = random.choice("abcdefghijklmnopqrstuvwxyz")
            printed_text[index] = choice

        else:
            choice = text[index]
            printed_text[index] = choice
            index += 1
            iter = 0

        print("".join(printed_text), end="\r")

        time.sleep(0.01)

        iter += 1

    return text

print(animate_text("Hello World. This type of Animation looks Very Cool", 6))