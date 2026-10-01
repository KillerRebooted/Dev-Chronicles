def sieve_of_eratosthenes(limit):
    # Smallest Prime Factor (SPF) array initialization
    spf = [i for i in range(limit + 1)]

    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            # Cross out all multiples of i, starting from i squared
            for j in range(i * i, limit + 1, i):
                # Only update if it hasn't already been crossed out by a smaller prime
                if spf[j] == j:
                    spf[j] = i

    return spf

def prime_factorise(num, spf=sieve_of_eratosthenes(3000)):
    prime_factors = set()

    while num != 1:
        prime_factors.add(spf[num])
        num //= spf[num]
        
    return prime_factors

def f(b, dp_cache):

    if b in dp_cache:
        return dp_cache[b]

    if 1 in b:
        dp_cache[b] = 1
        return 1
    
    if len(b) == 1:
        dp_cache[b] = b[0]
        return b[0]

    x1 = b[0]
    x2 = b[1]
    x2_factors = set(prime_factorise(x2))

    visited_states = [b]
    uncommon_factors = True
    while uncommon_factors:

        temp = (x1, x2)

        if temp in dp_cache:
            final_answer = dp_cache[temp]
            for state in visited_states:
                dp_cache[state] = final_answer
            return final_answer

        visited_states.append(temp)
        x1_factors = set(prime_factorise(x1))

        uncommon_factors = x1_factors - x2_factors

        if uncommon_factors:
            x1 -= 1

    if x1 == x2:
        final_answer = x1
    else:
        final_answer = f((x1-1, x2-1), dp_cache)

    for state in visited_states:
        dp_cache[state] = final_answer

    return final_answer

def main():

    MOD = 998244353

    T = int(input())

    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        f_b_sum = 0
        dp_cache = {}

        count = dict()
        count_size = 0

        for num in a:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                count_size += 1

        count = dict(sorted(count.items(), reverse=True))
        keys = list(count.keys())

        for idx1, i in enumerate(keys):

            f_b_sum = (f_b_sum + (pow(2, count[i], MOD) - 1)*f((i, ), dp_cache)) % MOD
            intermediate_perms = 1

            for idx2, j in enumerate(keys[idx1+1:]):
                b = (i, j)

                term_i = pow(2, count[i], MOD) - 1
                term_j = pow(2, count[j], MOD) - 1
                permutations = (term_i * term_j * intermediate_perms) % MOD

                f_b_sum = (f_b_sum + permutations*f(b, dp_cache)) % MOD

                intermediate_perms = (intermediate_perms * pow(2, count[j], MOD)) % MOD

        print(f_b_sum%MOD)

if __name__ == "__main__":

    main()