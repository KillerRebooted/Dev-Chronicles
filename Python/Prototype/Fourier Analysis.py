import cmath

def main():
    z = [
    1.0 + 1.0j, 
    0.0 + 1.0j, 
    -1.0 + 1.0j, 
    -1.0 + 0.0j, 
    -1.0 - 1.0j, 
    0.0 - 1.0j, 
    1.0 - 1.0j, 
    1.0 + 0.0j
    ]
    N = len(z)

    C = []

    for k in range(0, N//2 + 1):
        summation = 0
        for n in range(0, N-1+1):
            summation += z[n] * cmath.exp(-1j * ((2*cmath.pi*k*n)/N))
        Ck = summation/N
        C.insert(k, Ck)

    C.sort(key=lambda Ck: cmath.polar(Ck)[0], reverse=True)

    print(*[(Ck, cmath.polar(Ck)) for Ck in C], sep="\n")

if __name__ == "__main__":
    main()