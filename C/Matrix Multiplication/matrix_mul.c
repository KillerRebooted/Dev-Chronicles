#include <stdio.h>

void main() {
    int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int b[3][2] = {{10, 11}, {20, 21}, {30, 31}};
    int c[2][2];

    for (int i = 0; i < 2; i++) { // Rows of a
        for (int j = 0; j < 2; j++) { // Columns of b
            c[i][j] = 0;
            for (int k = 0; k < 3; k++) // Columns of a / Rows of b
                c[i][j] += a[i][k] * b[k][j];
        }
    }

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
}