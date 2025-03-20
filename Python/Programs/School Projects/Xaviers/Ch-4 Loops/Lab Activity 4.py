"""
Change Question to:-

Lab Activity Q.4 Check whether a given Number is a Prime Number or not.
"""

a = int(input("Enter a Number: ")) #Suppose 9

Prime = True

"""
We Start the Loop with 2 as 1 is already divisible by all Numbers. 
We End the Loop at 9 as we don't count the Number Itself
"""

for i in range(2, a):

    if a%i == 0: 
        
        """
        We check whether 9 is divisible by 'i' or not. If it even divides one Number, it is not a Prime Number and therefore set the Value of 'Prime' to False
        """

        Prime = False

"""
If 9 is not divisible by any Number between 2 - 8, 'Prime' will remain True
"""

if Prime == True:

    print(a, "is a Prime Number")

else:

    print(a, "is not a Prime Number")