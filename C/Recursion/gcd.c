#include <stdio.h>

int gcd(int a, int b) {
    int smaller = a<b?a:b;
    int bigger = a>b?a:b;
    
    if (bigger%smaller == 0)
        return smaller;

    return gcd(smaller, bigger%smaller);
}

void main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", gcd(a, b));
}