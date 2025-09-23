#include <stdio.h>

void main() {
    int a = 0, b = 1;
    int N;

    printf("Enter the Number of Terms (>= 2): ");
    scanf("%d", &N);

    printf("Fibonacci Series: %d %d ", a, b);
    for (int i = 3; i <= N; i++) {
        int c = a + b;
        a = b;
        b = c;
        printf("%d ", c);
    }
}