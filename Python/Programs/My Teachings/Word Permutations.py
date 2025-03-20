def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

def calculate_denominator(word):

    repetition = []

    unique_characters=""
    for char in word:
        if char not in unique_characters:
            unique_characters += char

    for i in unique_characters:
        repetition.append(word.count(i))

    num = 1

    for i in repetition:
        num *= factorial(i)

    return num


def permutations(word_list):

    perm = []

    for i in word_list:
        
        perm.append(factorial(len(i))//calculate_denominator(i))

    return perm

words = input("Enter the words separated by commas: ").split(",")

print(permutations(words))
