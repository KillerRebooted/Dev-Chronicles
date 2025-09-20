#include <stdio.h>

#define MIN(a,b) ((a)<(b)?(a):(b))

int gcd(int a, int b) {
    int rem;

    a = MIN(a,b);
    b = -MIN(-a,-b);

    while (1) {
        rem = b%a;
        if (rem == 0) {
            return a;
        }
        a = rem;
    }
}

int main() {
    int a, b;

    scanf("%d %d", &a, &b);
    printf("The GCD of %d and %d is %d\n", a, b, gcd(a, b));
}