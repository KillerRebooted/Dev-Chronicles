a = int(input("Enter a Number: "))        #Suppose 6
b = int(input("Enter another Number: "))  #Suppose 9

#HCF can't be Greater than 6 (Smaller of the 2 Numbers) and can't be smaller than 1

if a < b:

    smaller = a

else:

    smaller = b

#Checking all the Numbers between 6 (Smaller of the 2 Numbers) and 1 (not including 0)

while smaller > 0:

    if (a % smaller == 0) and (b % smaller == 0): #The first Number Divisible by both 'a' and 'b' is the HCF

        print()
        print("The HCF of", a, "and", b, "is", smaller)
        break #'break' stops the Loop as we don't require to Search an further

    smaller -= 1