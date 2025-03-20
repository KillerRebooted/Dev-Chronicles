num = int(input("Enter a Number: "))

for i in range(num + 1):

    print(f"{'*'*i}{' '*( (num*2)-(i*2) )}{'*'*i}")