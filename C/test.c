#include <stdio.h>

// [1 2 3 2 4], 5, i=0, currsum=0, target=4, subset, 0
void subsetSum(int set[], int n, int i, int currSum, int treasure, int subset[], int size) {
    if (i == n) // reached end
    {
        if (currSum == treasure)
        {
            for (int j = 0; j < size; j++)
                printf("%d ", subset[j]);
            printf("\n");
        }
        return;
    }

    // Include set[i]
    subset[size] = set[i];
    subsetSum(set, n, i + 1, currSum + set[i], treasure, subset, size + 1); // [1 2 3 2 4], 5, i=3, currsum=8, target=4, subset, size=4

    // Exclude set[i]
    subsetSum(set, n, i + 1, currSum, treasure, subset, size); // [1 2 3 2 4], 5, i=3, currsum=8, target=4, subset, size=4
}

int main() {
    int n, treasure;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int set[n];
    printf("Enter elements: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &set[i]);

    printf("Enter target sum: ");
    scanf("%d", &treasure);

    int subset[n];
    printf("\nSubsets with sum = %d:\n", treasure);
    subsetSum(set, n, 0, 0, treasure, subset, 0);
    return 0;
}