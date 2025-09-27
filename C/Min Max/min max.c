#include <stdio.h>

void main() {
    int arr[5] = {1,2,3,4,5};
    int min = arr[0];
    int max = arr[0];
    int min_idx = 0, max_idx = 0;

    for (int i = 0; i < 5; i++) {
        if (arr[i] < min) {
            min = arr[i];
            min_idx = i;
        }
        if (arr[i] > max) {
            max = arr[i];
            max_idx = i;
        }
    }

    int second_min = max;
    int second_max = min;
    for (int i = 0; i < 5; i++) {
        if (arr[i] < second_min && min_idx != i) {
            second_min = arr[i];
        }
        if (arr[i] > second_max && max_idx != i) {
            second_max = arr[i];
        }
    }

    printf("Min: %d, Second Min: %d\n", min, second_min);
    printf("Max: %d, Second Max: %d\n", max, second_max);
}