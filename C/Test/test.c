#include <stdio.h>

void main() {
    // This is a Comment
    int a=1, b=1, c;

    for (int i=1, N=20; i <= N; i++) {
        printf("%i\n", a);
        c = a+b;
        a = b;
        b = c;
    }
}