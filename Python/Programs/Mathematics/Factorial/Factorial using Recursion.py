def factorial(num):

    if num == 1:
        return num

    return num*factorial(num-1)

print(factorial(4))
print(factorial(5))
print(factorial(6))
