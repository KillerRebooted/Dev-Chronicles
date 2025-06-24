import math
from decimal import Decimal

def rev_digits(num):

    # n-1 < log(num) < n

    n = int(math.log(num, 10) + 1 - (math.log(num, 10)%1))

    # Summation

    rev_num = 0
    for k in range(n):
        rev_num += ((num*(Decimal(10)**(-k))%10) - (num*(Decimal(10)**(-k))%10)%1)*(Decimal(10)**(n-k-1))
    
    return rev_num

print(rev_digits(465))
print(rev_digits(6840))
print(rev_digits(3205))
print(rev_digits(100))
print(rev_digits(3205342801420398492033213454))