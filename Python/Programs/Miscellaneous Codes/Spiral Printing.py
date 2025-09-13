import math

n = int(input("Enter the Size of Spiral: "))

spiral = [[0]*n]
[spiral.append([0]*n) for _ in range(n-1)]

i = 0
j = 0

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
direction = 0

for num in range(1, n**2+1):
    spiral[i][j] = num

    i_add = directions[direction][0]
    j_add = directions[direction][1]

    if (i+i_add not in range(0, n)) or (j+j_add not in range(0, n)) or (spiral[i+i_add][j+j_add]):
        direction += 1
        direction %= 4
    
    i += directions[direction][0]
    j += directions[direction][1]

for i in spiral:
    for j in i:
        print(f"{j:3}", end=" ")
    print()