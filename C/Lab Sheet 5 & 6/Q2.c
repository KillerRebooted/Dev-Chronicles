#include <stdio.h>

void main() {
    int n;

    scanf("%d", &n);

    int arr[n];
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    int swap_dist = 2;

    // Using New Array
    int new_arr[n];
    for (int i=0; i<n; i++) {
        new_arr[i] = arr[(i+swap_dist)%n];
    }

    for (int i=0; i<n; i++) {
        printf("%d ", new_arr[i]);
    }
    printf("\n");
    
    // Using In Place Swapping
    /*
    for (int i=0; i<swap_dist%n; i++) {
        for (int j=0; j<n-1; j++) {
            arr[(j+1)%n] = arr[(j+1)%n]^arr[j];
            arr[j] = arr[(j+1)%n]^arr[j];
            arr[(j+1)%n] = arr[(j+1)%n]^arr[j];
        }
    }
    for (int i=0; i<n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    */
}