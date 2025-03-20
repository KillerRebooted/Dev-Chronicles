a = int(input("Enter a Number: "))
b = int(input("Enter the Power: "))

c = 1 #c = 1 because if we take c = 0, anything multiplied to it will also become 0

for i in range(b):

    c *= a #Shorter way to type c = c*a

print("The Number", a, "to the Power", b, "is", c)

#also a**b also gives the same answer