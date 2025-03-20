from sympy import *

AP = ["_", 2, "_", 12, "_", "_", "_"]

#An = a + (n-1)d

#2 = a + 1d
#a = 2-1d

#3 = a + 2d
#a = 3-2d

#  2a = 4-2d
#-  a = 3-2d
#   a = 1

new_list = []

for i in AP:

    if i != "_":

        new_list.append([i, AP.index(i)])

print(new_list)

d = Symbol("d")
a = Symbol("a")

eq1 = Eq(new_list[0][0] - new_list[0][1] * d, a)
eq2 = Eq(new_list[1][0] - new_list[1][1] * d, a)

solution = solve((eq1, eq2), (d, a))

New_AP = [AP[i] if AP[i] != "_" else solution[a] + i * solution[d] for i in range(len(AP))]

print(New_AP)