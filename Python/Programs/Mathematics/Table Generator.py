print()

from time import sleep

print("Hello my Fellow Human, if YOU also struggle in Tables just like me, so This Program is for YOU!!")

sleep(5)

print()
a = int(input("Enter the Number of which You want the Table to be Printed: "))
b = int(input("Enter the Number upto which You want the Table to be Printed: "))

print()

for x in range(1, b+1):
    print(f"{a} x {x} = {a * x}")
    sleep(0.3)

print()