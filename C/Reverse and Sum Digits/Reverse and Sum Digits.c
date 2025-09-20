#include <stdio.h>
#include <math.h>

void main() {
    int N, i, sum_digits=0, reversed_num=0;

    scanf("%d", &N);
    i = N;
    while (i!=0) {
        sum_digits += i%10;
        reversed_num = reversed_num * 10 + i%10;
        i /= 10;
    }
    printf("Sum of digits in %d is %d\n", N, sum_digits);
    printf("Reversed Number of %d is %d\n", N, reversed_num);
}