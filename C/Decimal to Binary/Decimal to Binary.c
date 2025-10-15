#include <stdio.h>

void main() {
    float n;
    int arr[16] = {0};
    scanf("%f", &n);
    int I = n;
    float fI = n - I;

    for (int i = 7; i >= 0; i--) {
        arr[i] = I % 2;
        I /= 2;
        if (I == 0)
            break;
    }

    for (int i = 8; i <= 15; i++) {
        arr[i] = 2 * fI;
        fI = 2 * fI - arr[i];
    }

    for (int i = 0; i <= 15; i++) {
        printf("%d", arr[i]);
        if (i == 7)
            printf(".");
    }
}