#include <stdio.h>

void main() {
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int t_matrix[3][2];

    for (int i = 0; i <= 1; i++) {
        for (int j = 0; j <= 2; j++) {
		t_matrix[j][i] = matrix[i][j];
	}
    }

    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 1; j++) {
		printf("%d", t_matrix[i][j]);
	}
	printf("\n");
    }

}