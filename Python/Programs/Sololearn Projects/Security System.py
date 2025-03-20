layout = input("Enter: ")
a = ""
for i in layout:
    if i not in "xGT$":
        print("Invalid")
        quit()
    if i in "GT$":
        a += i

#xxxGxxxTxxGxx$
#x = Empty Floor
#G = Guard
#T = Thief
#$ = Money
#if G between T and $, quiet
#else ALARM

x = a.index("$")
y = a.index("T")

if x-y == 1 or x-y == -1:
    print("ALARM")

else:

    print("quiet")
