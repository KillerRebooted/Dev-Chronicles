#include <stdio.h>
#include <math.h>

int determinant(int n, int arr[n][n], int det) {

    if (n==1)
        return arr[0][0];

    for (int j=0; j<n; j++) {

        int temp_arr[n-1][n-1];

        int r=0, c=0;
        for (int k=1; k<n; k++) {
            for (int l=0; l<n; l++) {
                if (j==l)
                    continue;
                temp_arr[r][c] = arr[k][l];
                printf("%d ", arr[k][l]);
                c += 1;
                c %= n;
                if (c==0)
                    r += 1;
            }
            printf("\n");
        }

        det += arr[0][j]*pow(-1, j)*determinant(n-1, temp_arr, 0);
    }

    return det;

}

int cofactor(int n, int arr[n][n]) {

    int co_matrix[n][n];

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            int temp_arr[n-1][n-1];

            int r=0, c=0;
            for (int k=0; k<n; k++) {
                for (int l=0; l<n; l++) {
                    if (i==k || j==l)
                        continue;
                    temp_arr[r][c] = arr[k][l];
                    c += 1;
                    c %= n;
                    if (c==0)
                        r += 1;
                }
            }

            co_matrix[i][j] = determinant(n-1, temp_arr, 0)*pow(-1, i+j);
        }
    }

    printf("\nThe Co-Factor Matrix is:\n");
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            printf("%d ", co_matrix[i][j]);
        }
        printf("\n");
    }

}

int main() {
    int n;

    printf("Enter the Size of the Matrix: ");
    scanf("%d", &n);

    int arr[n][n];

    printf("\nEnter the Values for %dx%d Matrix:\n", n, n);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    cofactor(n, arr);

}