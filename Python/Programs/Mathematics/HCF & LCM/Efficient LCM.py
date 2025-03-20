from os import system

clear = lambda: system("cls")

clear()

def HCF(Numbers):

    global hcf
    global OG_Numbers

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

Numbers = input("Enter the Numbers separated by commas: ").split(",")

HCF(Numbers)

OG_Numbers_New = OG_Numbers

lcm = OG_Numbers_New[0]

for i in range(1, len(OG_Numbers_New)):

    HCF([ str(lcm), str(OG_Numbers_New[i]) ])

    lcm = int((lcm*OG_Numbers_New[i]) // hcf)

print(f"\nThe LCM of the Number(s) {str(OG_Numbers_New).replace('[', '').replace(']', '')} is \033[1m{lcm}\033[0m\n")