#include <stdio.h>

int factorial(int x) {
    if (x == 1) {
        return 1;
    }
    return x*factorial(x-1);
}

void main() {
    int n = 30;
    printf("%d! = %d\n", n, factorial(n));
}