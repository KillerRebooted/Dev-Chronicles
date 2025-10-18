#include <stdio.h>

float power(int n, int x) {
    if (x == 1)
        return n;
    if (x == 0)
        return 1;
    return n*power(n, x-1);
}

int factorial(int n) {
    if (n == 1 || n == 0) {
        return 1;
    }
    return n*factorial(n-1);
}

float sine(int x, int n) {
    if (n == 0)
        return 0;
    float term = power(-1, n+1)*power(x, 2*n-1)/factorial(2*n-1);
    return term + sine(x, n-1);
}

float cosine(int x, int n) {
    if (n == 0)
        return 0;
    float term = power(-1, n+1)*power(x, 2*n-2)/factorial(2*n-2);
    return term + cosine(x, n-1);
}

float taylor_sum(int x, int n) {
    return sine(x, n) + cosine(x, n);
}

void main() {
    printf("%Lf", taylor_sum(10, 10));
}