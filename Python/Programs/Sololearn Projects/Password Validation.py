Password = input("Enter Your Password: ")

num = 0
symbol = 0

for i in Password:

    if i.isdigit():

        num += 1

    if i in "!@#$%&*":

        symbol += 1

if (num >= 2) and (symbol >= 2) and (len(Password) >= 7):

    print("Strong")

else:

    print("Weak")
