#include <stdio.h>

void main() {
    int N=10, sum=0;
    for (; N>=1; N--) {
        printf("%d, %d\n", N, sum);
        sum += N;
    }
    printf("Sum of Numbers upto %d is %d", N, sum);

    /*N = 6;
    int factorial = 1;
    do {
        factorial *= N;
        N--;
    } while (N>1);

    printf("%d\n", factorial);
    */

}