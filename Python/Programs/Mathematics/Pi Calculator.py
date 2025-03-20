from decimal import Decimal
from os import system

clear = lambda: system('cls')

clear()

Num = 3

x = int(input("""How many times to repeat the Calculation?
The Higher the Number, the more close the Number is to the Value of Pi but longer the time to Calculate....
Maybe after 1 Million or so, the difference might be unnoticable so don't repeat further than 1 Million if you just want the value of Pi
If you want to test the capabilities of the Program, You are Free to enter any Number, Progress Bar will be Showed :)

Type the Number: """))

clear()

a = 0
b = 1
c = 2

OgNum = x

space = ' '*len(str(x))

e = int(OgNum/100)

print(int(100-(x/OgNum *100)), r"% of ", OgNum, "\n[", "="*int(100-(x/OgNum *100)), " "*int(x/OgNum *100), "]", '\n' , x, "left", space, end = "\r")

while x != 0:

    a += 2
    b += 2
    c += 2

    d = a*b*c
    
    Num += Decimal('4')/Decimal(d)

    a += 2
    b += 2
    c += 2

    d = a*b*c
    
    Num -= Decimal('4')/Decimal(d)

    e -= 1
    x -= 1

    if e == 0:
        clear()
        print(int(100-(x/OgNum *100)), r"% of ", OgNum, "\n[", "="*int(100-(x/OgNum *100)), " "*int(x/OgNum *100), "]", '\n' , x, "left", space, end = "\r")
        e = int(OgNum/100)
    

clear()
print(int(100-(x/OgNum *100)), r"% of ", OgNum, "\n[", "="*int(100-(x/OgNum *100)), " "*int(x/OgNum *100), "]", '\n' , x, "left", space)
print('\n', f"The Value of Pi is {Num}")
