a = input("Enter a series of Letters: ")

x = 0

for i in a:

    if a.count(i) > 1:

        print("Deja Vu")
        quit()

    else:

        x = 0

print("Unique")
