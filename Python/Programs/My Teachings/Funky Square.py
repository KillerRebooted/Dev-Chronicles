num = int(input("Enter a Number: "))

line = " "

for i in range(num):

    line = line[:i] + f"{i+1}" * (num-i)
    
    print(line)
