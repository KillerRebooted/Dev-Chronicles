def prime_factorise(num):
    prime_factors = []
    test_prime = 2
    
    # We only need to check up to the square root of the number
    while test_prime * test_prime <= num:
        if num % test_prime == 0:
            prime_factors.append(test_prime)
            num //= test_prime
        else:
            # If not divisible by 2, skip even numbers. Otherwise, just add 1.
            test_prime += 1 if test_prime == 2 else 2
            
    # If num is greater than 1 at the end, it must be prime itself
    if num > 1:
        prime_factors.append(num)
        
    return prime_factors

def f(b):
    if 1 in b:
        return 1
    
    if len(b) == 1:
        return b[0]

    x1 = min(b)
    x2 = max(b)
    uncommon_factors = True
    while uncommon_factors:

        x1_factors = set(prime_factorise(x1))
        x2_factors = set(prime_factorise(x2))

        uncommon_factors = x2_factors - x1_factors

        if uncommon_factors:
            x2 -= 1

    if x1 == x2:
        return x1

    return f([x1-1, x2-1])

def main():

    T = int(input())

    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        f_b_sum = 0

        count = dict()
        count_size = 0

        for num in a:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                count_size += 1

        count = dict(sorted(count.items()))

        for idx1, i in enumerate(list(count.keys())):
            f_b_sum += (2**count[i] - 1)*f([i])
            for idx2, j in enumerate(list(count.keys())[idx1+1:]):
                b = [i, j]
                intermediate_counts = [count[x] for x in list(count.keys())[idx1+1:idx1+1+idx2]]
                permutations = 1
                for power in intermediate_counts:
                    permutations *= 2**power
                permutations *= (2**count[i]-1) * (2**count[j]-1)
                f_b_sum += permutations*f(b)

        print(f_b_sum%998244353)

if __name__ == "__main__":

    main()