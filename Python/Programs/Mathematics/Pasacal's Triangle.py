import pandas as pd

def f(x):
    if x == 1:
        return x
    if x == 0:
        return 1

    return x*f(x-1)

def C(n, r):
    if n<r:
        raise "Invalid Value for 'n' and 'r'. 'n' must be >= 'r' and <= 'n"
    return (f(n))//((f(r))*(f(n-r)))

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[ ::2] = lst
    return result

n = int(input("Enter the Number of Rows: "))

df = pd.DataFrame()

for row in range(n):
    value = ""

    for i in range(row+1):
        if i != row: value += str(C(row, i)) + " "
        else: value += str(C(row, i))

    df[row] = list(" "*(n-row-1)) + intersperse(value.split(), " ") + list(" "*(n-len(value.split())))

df.index = [""]*df.shape[0]
pascals_triangle = df.T.to_string(index=False)

print(pascals_triangle)