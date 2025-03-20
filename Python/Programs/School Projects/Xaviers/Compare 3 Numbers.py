Num1 = float(input("Enter a Number: "))
Num2 = float(input("Enter another Number: "))
Num3 = float(input("Enter one LAST Number: "))

if (Num1 == Num2) and (Num2 == Num3):
    print("Don't try to fool ME! Enter Different Numbers.")

print()

if (Num1 >= Num2) and (Num1 >= Num3):
    print(f"{Num1} is the Greatest Number")

elif (Num2 >= Num1) and (Num2 >= Num3):
    print(f"{Num2} is the Greatest Number")

elif (Num3 >= Num1) and (Num3 >= Num2):
    print(f"{Num3} is the Greatest Number")


if (Num1 <= Num2) and (Num1 <= Num3):
    print(f"{Num1} is the Smallest Number")

elif (Num2 <= Num1) and (Num2 <= Num3):
    print(f"{Num2} is the Smallest Number")

elif (Num3 <= Num1) and (Num3 <= Num2):
    print(f"{Num3} is the Smallest Number")
