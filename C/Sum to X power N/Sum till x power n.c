#include <stdio.h>

void main() {
    int x, n;
    float multiply, ans, sum = 0;

    printf("Enter the value of x and n: ");
    scanf("%d %d", &x, &n);

    if (n < 0) {
        multiply = 1.0/x; 
        n *= -1;
    }
    else {
        multiply = x;
    }

    for (int i = 0; i <= n; i++) {
        ans = 1;
        for (int j = 1; j <= i; j++) {
            ans *= multiply;
        }
        sum += ans;
    }

    printf("Sum from %d^0 to %d^%d is %f", x, x, n, sum);
}