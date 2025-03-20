a = input("Enter a Number: ")
b = input("Enter another Number: ")

if (not a.isdigit()) or (not b.isdigit()):

    raise Exception("Baka")

a = int(a)
b = int(b)

if (a <= 1) or (b <= 1):

    raise Exception("Baka")

print()
print("All Prime Numbers between", a, "and", b, "are: ")

for i in range(a, b+1):

    Prime = True

    for j in range(2, i):

        if i % j == 0:

            Prime = False

    if Prime == True:

        print(i)