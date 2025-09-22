#include <stdio.h>

void main() {
    int N;
    int directions[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};  // right, down, left, up
    int dir = -1;

    printf("Enter the Size of the Spiral: ");
    scanf("%d", &N);

    int r=0, c=0, r_add, c_add;
    int spiral[N][N];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            spiral[i][j] = 0;
        }
    }

    for (int i = 1; i <= N*N; i++) {

        if ((r + r_add < 0) || (r + r_add >= N) || (c + c_add < 0) || (c + c_add >= N) || spiral[r + r_add][c + c_add]) {
            dir += 1;
            dir %= 4;
            r_add = directions[dir][0];
            c_add = directions[dir][1];
        }

        spiral[r][c] = i;

        r += r_add;
        c += c_add;
    }

    printf("\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%3d ", spiral[i][j]);
        }
        printf("\n");
    }

}