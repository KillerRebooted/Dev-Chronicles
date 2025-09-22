#include <stdio.h>

void main() {
    int N, r, c;

    printf("Enter the Size of the Magic Square (Odd Number): ");
    scanf("%d", &N);

    int magic_square[N][N];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            magic_square[i][j] = 0;
        }
    }

    r = 1;
    c = N/2-1;
    for (int i = 1; i <= N*N; i++) {

        if (magic_square[(r+N-1)%N][(c+N+1)%N] != 0) {
            r = (r+N+1)%N;
        }
        else {
            r = (r+N-1)%N;
            c = (c+N+1)%N;
        }

        magic_square[r][c] = i;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%3d ", magic_square[i][j]);
        }
        printf("\n");
    }

}