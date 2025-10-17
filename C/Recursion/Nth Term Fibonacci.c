#include <stdio.h>

int fibn(int n) {
    if (n==0 || n==1) {
        return 1;
    }
    return fibn(n-1) + fibn(n-2);
}

void main() {
    printf("%d", fibn(5));
}