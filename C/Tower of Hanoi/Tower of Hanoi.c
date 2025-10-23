#include<stdio.h>

void TOH(int n, int from, int aux, int to) {
    if (n == 1)
        printf("Move a disc from Node %d to %d\n", from, to);
    else {
        // Moving n-1 Disks from FROM to AUX
        TOH(n-1, from, to, aux);
        // Moving Last Disk from FROM to TO
        printf("Move a disc from Node %d to %d\n", from, to);
        // Moving n-1 Disks from AUX to TO
        TOH(n-1, aux, from, to);
    }
}

void main() {
    int n = 3, from=1, aux=2, to=3;

    printf("Enter Size of the Tower: ");
    scanf("%d", &n);

    TOH(n, from, aux, to);
}