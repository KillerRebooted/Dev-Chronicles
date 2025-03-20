Num = input("Enter a Number: ")

try:
    float(Num)

except:
    print("Invalid Input")
    exit()

if Num[-1] == "7":
    print("Ends with 7")

else:
    print("Does not End with 7")

#Alternate Answer
"""if Num%10 == 7:
    print("Ends with 7")

else:
    print("Does not End with 7")"""
