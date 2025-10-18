#include <stdio.h>
#include <math.h>

double power(double n, int x) {
    if (x == 1)
        return n;
    if (x == 0)
        return 1;
    return n*power(n, x-1);
}

long int factorial(int n) {
    if (n == 1 || n == 0) {
        return 1;
    }
    return n*factorial(n-1);
}

double sine(double x, int n) {
    if (n == 0)
        return 0;
    double term = power(-1, n+1)*power(x, 2*n-1)/factorial(2*n-1);
    return term + sine(x, n-1);
}

double cosine(double x, int n) {
    if (n == 0)
        return 0;
    double term = power(-1, n+1)*power(x, 2*n-2)/factorial(2*n-2);
    return term + cosine(x, n-1);
}

double taylor_sum(double x, int n) {
    return sine(x, n) + cosine(x, n);
}

void main() {
    double n = 13, x = (M_PI/6);
    printf("sin(%lf) = %lf, cos(%lf) = %lf, sin(%lf)+cos(%lf) = %lf", x, sine(x, n), x, cosine(x, n), x, x, taylor_sum(x, n));
}