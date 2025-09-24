#include <stdio.h>

void main() {
    float x, numerator;
    int n, denominator;

    printf("Enter the value of x and n: ");
    scanf("%f %d", &x, &n);

    double sum = 0;
    for (int i = 0; i < n; i++) {
        numerator = 1, denominator = 1;
        for (int j = 1; j <= i; j++) {
            numerator *= x;
            denominator *= j;
        }
        sum += numerator/denominator;
    }

    printf("The value of e^%f upto %d terms is %lf", x, n, sum);

}