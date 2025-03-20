a = int(input("Enter a Number: "))

print()
print("All Factors of", a, "are: ")

for i in range(1, a+1): #a + 1 as 'a' is not included

    if a % i == 0:

        print(i)