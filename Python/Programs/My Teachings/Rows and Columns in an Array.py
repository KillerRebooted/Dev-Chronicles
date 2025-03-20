rows = 4
columns = 3

# Starting number
x = 1

# Step size
y = 2

array = []
num = 1

for i in range(rows):
    list = []
    for j in range(columns):
        list.append(num)

        num += y

    array.append(list)

print(array)
