newl = [1, 8, 10, 16, 19, 22, 27, 33, 36, 40, 47, 52, 56, 61, 63, 71, 72, 75, 81, 81, 84, 88, 96, 98, 103, 110, 113, 118, 124, 128, 129, 134, 134, 139, 148, 157, 157, 160, 162, 164]

#Method 1
result = list(zip(newl, newl[1:]))

print(result)

#Method 2
lst = []

for i in range(len(newl)):
    try:
        lst.append((newl[i], newl[i+1]))
    except:
        pass

print(lst)

#Both are Correct
print(lst==result)
