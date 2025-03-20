import random

n = int(input("Enter a Number: "))

random_nums = [random.randint(33,127) for i in range(n*n)] 
matrix = [chr(i) for i in random_nums]

print(matrix, len(matrix))
