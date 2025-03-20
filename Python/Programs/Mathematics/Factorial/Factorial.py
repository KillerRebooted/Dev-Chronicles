n = None

while n!=0:
    
    print()
    Num = int(input("Enter a Number (0 to Quit): "))
    n = Num

    Factorial = 1

    if n<=0:
        print("See Ya!")

    else:
        
        while Num!=0:
            Factorial *= Num
            Num -= 1

        print(f"The Factorial of {n} is {Factorial}")
