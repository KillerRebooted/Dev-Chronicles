#include <stdio.h>

void check_subsets(int n, int *arr, int req_sum) {
    int sub_arr[n];
    for (int i = 0; i < n; i++) {
        sub_arr[i] = 0;
    }

    for (int i = 0; i < (1 << n); i++) {

        int carry = 1;
        for (int j = n-1; j >= 0; j--) {
            sub_arr[j] += carry;
            carry = sub_arr[j]/2;
            sub_arr[j] %= 2;
        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (sub_arr[i])
                sum += arr[i];
        }

        if (sum == req_sum) {
            for (int i = 0; i < n; i++) {
                if (sub_arr[i]) {
                    printf("%d ", arr[i]);
                }
            }
            printf("\n");
        }
    }
}

void main() {
    int n;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", arr+i);
    }

    int req_sum;
    printf("Enter the required subset sum: ");
    scanf("%d", &req_sum);

    printf("\n");

    printf("The subsets with sum %d are:\n", req_sum);
    check_subsets(n, arr, req_sum);

}