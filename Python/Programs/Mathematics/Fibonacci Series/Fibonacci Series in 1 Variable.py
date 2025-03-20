from os import system

clear = lambda: system('cls')

clear()

num = input("Enter the Number till which you want the Series to be printed (>= 2): ")

if (num.isdigit() == False) or (int(num) < 2):

    print()
    raise Exception("Baka\n")

List = [0, 1]

print(f"\n{1}")

for i in range(int(num)-1):

    List.append(List[-1] + List[-2])

    print(List[-1])

print()