#include <stdio.h>

int check(int n, int arr[n], int value) {
    for (int i=0; i<n; i++) {
        if (arr[i] == value) {
            return i;
        }
    }
    return -1;
}

void main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    int count_value[n];
    int count[n];

    for (int i=0; i<n; i++) {
        count_value[i] = 0;
        count[i] = 0;
    }

    for (int i=0; i<n; i++) {
        int idx = check(n, count_value, arr[i]);
        if (idx != -1) {
            count[idx] += 1;
        }
        else {
            int idx = check(n, count, 0);
            count_value[idx] = arr[i];
            count[idx] = 1;
        }
    }

    for (int i=0; i<n; i++) {
        if (!count[i])
            break;
        printf("%d occurs %d times\n", count_value[i], count[i]);
    }
}