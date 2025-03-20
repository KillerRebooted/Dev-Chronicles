import math

a = input("Enter a String: ")

al = 0

for i in a:

    if i.isalpha():
        al += 1

print(math.ceil(al / len(a.split())) )
