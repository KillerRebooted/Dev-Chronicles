a = int(input("Enter a Number: "))        #Suppose 6
b = int(input("Enter another Number: "))  #Suppose 9

#LCM can be Lesser than 9 (Greater of the 2 Numbers) and it can't be Greater than 54 (6*9)

if a > b:

    greater = a

else:

    greater = b

for i in range(greater, (a*b)+1):

    if (i % a == 0) and (i % b == 0): #The first Number Divisible by both 'a' and 'b' is the LCM

        print()
        print("The LCM of", a, "and", b, "is", i)
        break   #'break' stops the Loop as we don't require to Search an further