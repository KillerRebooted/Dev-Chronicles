import sys

print("Hello World!\n")

def inp(Variable, Sentence, Exception):

    global a

    a = {}
    
    x = "0"

    while x not in Exception:

        x = input(Sentence)

        if x not in Exception:

            sys.stdout.write("\033[F")
            print(" "*len(Sentence + x))
            sys.stdout.write("\033[F")

    a[Variable] = x

    return ""

inp("Hello", "Enter: ", "abcdABCD")

print(a["Hello"])