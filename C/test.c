#include <stdio.h>

int factorial(int n) {
    if (n == 1 || n == 0) {
        return 1;
    }
    return n*factorial(n-1);
}

int C(int n, int r) {
    return (factorial(n) / (factorial(r) * factorial(n - r)));
}

void main() {
    int size;

    printf("Enter the Size of Pascal's Triangle: ");
    scanf("%d", &size);

    printf("\nPascal's Triangle using C(n, r) Function:\n\n");
    for (int n=0; n<size; n++) {
        for (int i=0; i<size-n-1; i++) printf(" ");
        for (int r=0; r<=n; r++) {
            printf("%d ", C(n, r));
        }
        printf("\n");
    }

    printf("\nPascal's Triangle using 2D Arrays:\n\n");
    int pascal[size][size];
    for (int r=0; r<size; r++) {
        for (int i=0; i<size-r-1; i++) printf(" ");
        for (int c=0; c<=r; c++) {
            if (c==0 || c==r)
                pascal[r][c] = 1;
            else
                pascal[r][c] = pascal[r-1][c-1] + pascal[r-1][c];
            printf("%d ", pascal[r][c]);
        }
        printf("\n");
    }
}