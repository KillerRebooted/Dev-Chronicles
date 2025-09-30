#include <stdio.h>

void main() {
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int sum = 0;

    for (int i = 0; i <= 1; i++) {
        sum = 0;
        for (int j = 0; j <= 2; j++) {
            sum += matrix[i][j];
        }
        printf("Row %d: %d\n", i+1, sum);
        }

    for (int i = 0; i <= 2; i++) {
        sum = 0;
        for (int j = 0; j <= 1; j++) {
            sum += matrix[j][i];
        }
        printf("Column %d: %d\n", i+1, sum);
    }

}