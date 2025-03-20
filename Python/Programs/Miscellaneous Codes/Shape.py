x=0
y=int(input("Enter an Integer: "))
while x<y:

    z=0

    while z<y:

        print("*  ", end="")
        z+=1

    print("\n", end="\r")
    x+=1