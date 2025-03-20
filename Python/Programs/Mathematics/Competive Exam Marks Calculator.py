import decimal, sys

decimal.getcontext().prec = 60
sys.setrecursionlimit(1500)

mm = 300
marks_per_question = 4
negative = 1
questions = mm//marks_per_question

def factorial(x):
    if x == 0:
        return 1
    return x*factorial(x-1)

def C(n, r):
    return decimal.Decimal(factorial(n)) / decimal.Decimal((factorial(r))*(factorial(n-r)))

total_possibilities = 0
total_marks = {marks:0 for marks in range(questions*-negative, questions*marks_per_question+1)}

for question in range(0, questions+1):
    
    correct_possibilities = C(questions, question)
    marks = question*marks_per_question

    remaining_questions = questions-question

    for incorrect_question in range(0, remaining_questions+1):

        wrong_possibilities = C(remaining_questions, incorrect_question)

        total_possibilities += decimal.Decimal(correct_possibilities*wrong_possibilities)
        total_marks[marks - incorrect_question*negative] += decimal.Decimal(correct_possibilities*wrong_possibilities)

print(total_possibilities, "\n")

for k, v in total_marks.items():
    print(f"{k}: {v}")

print(f"\nProbabillity of getting 206 Marks: {(total_marks[206]/total_possibilities * 100)}%")