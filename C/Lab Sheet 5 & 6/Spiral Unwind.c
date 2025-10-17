#include <stdio.h>

void main() {
    int n;

    printf("Enter the Matrix Size: ");
    scanf("%d", &n);

    int spiral[n][n];
    int unwind[n*n];

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {    
            scanf("%d", &spiral[i][j]);
        }
    }

    int row = 0, column = -1;
    int directions[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int dir = 0;

    int r_add=0, c_add=1, dummy_steps=n, steps=n;
    for (int i=0; i<n*n; i++) {
        
        row += r_add;
        column += c_add;
        unwind[i] = spiral[row][column];
        
        dummy_steps -= 1;
        if (!dummy_steps) {
            if (dir==0 || dir==2) {
                steps -= 1;
            }
            dummy_steps = steps;

            dir = (dir+1)%4;
            r_add = directions[dir][0];
            c_add = directions[dir][1];
        }

        //printf("Value: %d, Row: %d, Column: %d, Steps: %d, Dummy Steps: %d, Direction: %d\n", unwind[i], row, column, steps, dummy_steps, dir);
        
        printf("%d ", unwind[i]);

    }
}