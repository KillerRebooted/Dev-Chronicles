#Take the digits that completely divide the whole Number and print it in reverse

num = input("Enter a Number: ")
new_num = ""

for i in num:

    if int(num)%int(i) == 0:
        new_num += i

print(new_num[::-1])
