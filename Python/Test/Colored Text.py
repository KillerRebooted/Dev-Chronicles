from time import sleep

def RGB(txt, Cycles):

    def colored(r, g, b, txt):
        return f"\033[38;2;{r};{g};{b}m{txt} \033[38;2;255;255;255m"

    r = 255
    g = 0
    b = 0
    x = 0

    while x != Cycles:

        while g != 255:

            print(colored(r, g, b, txt), end="\r")
            sleep(0.1)

            g += 51

        while r != 0:

            print(colored(r, g, b, txt), end="\r")
            sleep(0.1)

            r -= 51

        while b != 255:

            print(colored(r, g, b, txt), end="\r")
            sleep(0.1)

            b += 51

        while g != 0:

            print(colored(r, g, b, txt), end="\r")
            sleep(0.1)

            g -= 51

        while r != 255:

            print(colored(r, g, b, txt), end="\r")
            sleep(0.1)

            r += 51

        while b != 0:

            print(colored(r, g, b, txt), end="\r")
            sleep(0.1)

            b -= 51

        x += 1

    print(f"\033[38;2;{r};{g};{b}m{txt} \033[38;2;255;255;255m")

RGB("Hello World", 2)