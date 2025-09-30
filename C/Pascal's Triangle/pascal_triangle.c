#include <stdio.h>

void main() {
    int n = 7;
    int pascal[7][7];

    for (int col = 0; col < 7; col++) {
        for (int row = 0; row < 7; row++) {
            if ((col == 0) || (row == col)){
                pascal[row][col] = 1;
                continue;
            }
            if (row < col) {
                pascal[row][col] = 0;
                continue;
            }
            pascal[row][col] = pascal[row-1][col-1] + pascal[row-1][col];
        }
    }

    for (int row = 0; row < 7; row++) {
        int spaces = ((7+6)-(row+1)-(row))/2;
        spaces = (7-row);
        for (int i = 0; i <= spaces; i++) {
            printf("  ");
        }
        for (int col = 0; col <= row; col++) {
            printf("%3d ", pascal[row][col]);
        }
        printf("\n");
    }

}