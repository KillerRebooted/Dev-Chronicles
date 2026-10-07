from functools import lru_cache

@lru_cache(maxsize=None)
def M(n, p):
    if n <= 1:
        return (n, 0)
    if p == 3:
        return (2**n - 1, n-1)
    
    minimum = float("inf")
    best_k = 1
    for k in range(1, n):
        temp = 2*M(k, p)[0] + M(n-k, p-1)[0]
        if temp < minimum:
            minimum = temp
            best_k = k

    return (minimum, best_k)

def moves(k):
    if n <= 1:
        return (n, 0)
    if p == 3:
        return (2**n - 1, n-1)

    print(2*M(k, p)[0] + M(n-k, p-1)[0])

n = int(input("Enter the number of Disks: "))
p = int(input("Enter the number of Pegs: "))

moves(M(n, p)[1])