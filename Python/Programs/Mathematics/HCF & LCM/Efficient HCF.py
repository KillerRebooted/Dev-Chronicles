from os import system

clear = lambda: system("cls")

clear()

def HCF():

    global hcf
    global OG_Numbers

    Numbers = input("Enter the Numbers separated by commas: ").split(",")

    for i in range(len(Numbers)):

        if Numbers[i].strip().isdigit() == False:

            print()
            raise Exception("Baka\n")

        else:

            Numbers[i] = int(Numbers[i].strip())

    OG_Numbers = Numbers.copy()

    if len(Numbers) == 1:

        hcf = Numbers[0]

    else:

        Divisor = min(Numbers)
        Numbers.remove(Divisor)

        Dividend = min(Numbers)
        Numbers.remove(Dividend)

        while True:

            while Dividend%Divisor != 0:

                Divisor, Dividend = Dividend%Divisor, Divisor

            hcf = Divisor

            if len(Numbers) != 0:

                Dividend = min(Numbers)

                Numbers.remove(Dividend)

            else:

                break

HCF()
print(f"\nThe HCF of the Number(s) {str(OG_Numbers).replace('[', '').replace(']', '')} is \033[1m{hcf}\033[0m\n")