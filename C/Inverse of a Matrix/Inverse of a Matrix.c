#include <stdio.h>

// Display a given mxn Matrix
void display_matrix(int m, int n, double matrix[m][n]) {

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%12lg ", matrix[i][j]);
        }
        printf("\n");
    }

}

// Executing Elementary Row Operations on given Rows
void row_operation(int n, double pivot_row[n], double row[n], double mul_factor) {
    double temp;

    // mul_factor = 0 for Row Swap
    // Same pivot_row and row for Scalar Row Multiplication

    if (mul_factor == 0) {
        for (int i = 0; i < n; i++) {
            temp = pivot_row[i];
            pivot_row[i] = row[i];
            row[i] = temp; 
        }
    }
    else if (pivot_row != row) {
        for (int i = 0; i < n; i++) {
            row[i] += pivot_row[i]*mul_factor;
        }
    }
    else {
        for (int i = 0; i < n; i++) {
            pivot_row[i] *= mul_factor;
        }
    }

}

// Calculate Inverse of a Matrix
void inverse_matrix(int n, double matrix[n][n], double inverse[n][n]) {
    double augmented[n][2*n];

    // Creating Augmented Matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            augmented[i][j] = matrix[i][j];
        }
        for (int j = 0; j < n; j++) {
            if (i == j) 
                augmented[i][n+j] = 1;
            else
                augmented[i][n+j] = 0;
        }
    }

    // Elementary Row Operations
    int max;
    for (int i = 0; i < n; i++) {
        
        max = i;
        for (int j = i; j < n; j++) {
            long double current = augmented[j][i] < 0 ? -augmented[j][i] : augmented[j][i];
            long double max_val = augmented[max][i] < 0 ? -augmented[max][i] : augmented[max][i];

            if (current > max_val) max = j;
        }
        if (i != max) row_operation(2*n, augmented[i], augmented[max], 0); // Swap Rows for Partial Pivoting
        
        row_operation(2*n, augmented[i], augmented[i], 1/augmented[i][i]);
        for (int j = 0; j < n; j++) {
            if (i == j || augmented[j][i] == 0) continue;
            row_operation(2*n, augmented[i], augmented[j], -augmented[j][i]);
        }

    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            inverse[i][j] = augmented[i][n+j];
        }
    }

}

void main() {
    int n;

    printf("Enter the size of the matrix: ");
    scanf("%d", &n);

    double matrix[n][n], inverse[n][n];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &matrix[i][j]);
        }
    }

    printf("\n\nOriginal Matrix: \n\n");
    display_matrix(n, n, matrix);

    inverse_matrix(n, matrix, inverse);

    printf("\n\nInverse Matrix: \n\n");
    display_matrix(n, n, inverse);

}