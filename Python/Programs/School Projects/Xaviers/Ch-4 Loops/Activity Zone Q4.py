"""
a) Explanation:

Here we are adding the Value of 'a' if it is Divisble by 5
s is the sum of all the Multiples of 5 between 20 and 100
100 + 95 + 90 + .... 25 + 20 = 1020
"""

print("Q4 a)\n")

a = 100              #Code Starts
b = 20
s = 0

while a >= b:

    if a%5 == 0:

        s += a

    a -= 1

print(s)             #Code Ends

print("\n"*5)

"""
b) Explanation
Here we are printing n*n which is the square of n
Then we add 1 to 'n' and keep printing squares until 'n' becomes 4 (5 is not included in 'while n < 5')
"""

print("Q4 b)\n")

n = 1                   #Code Starts

while n < 5:

    print(n*n)
    n += 1

print("Program Over")   #Code Ends

print("\n"*5)

"""
c) Explanation
Here we print n+n (basically 2*n)
Then we add 10 to 'n' and repeat the Process until n becomes 40 (50 not included in 'while n < 50')
"""

print("Q4 c)\n")

n = 10                  #Code Starts

while n < 50:

    print(n+n)

    n += 10

print("Program Over")   #Code Ends