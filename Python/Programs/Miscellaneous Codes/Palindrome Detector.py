print()
Palindrome = input("Type a Word, and I, 'THE SUPER COMPUTER' will Detect whether it's a Palindrome or not: ")

Check = len(Palindrome)//2

print()

from time import sleep

for x in range(Check):

    if Palindrome[Check] == Palindrome[-Check -1]:
        print("Checking   ", end="\r")
        sleep(0.2)
        print("Checking.  ", end="\r")
        sleep(0.2)
        print("Checking.. ", end="\r")
        sleep(0.2)
        print("Checking...", end="\r")
        sleep(0.2)
    
        Check = Check - 1

    else:
        print("This is NOT a Palindrome, I mean, You were expecting this Answer. Weren't You??")
        print()
        exit()

print("This is a VERIFIED Palindrome by 'THE SUPER COMPUTER', You Definitely were Attentinve in your Grammar Classes!!")
print()