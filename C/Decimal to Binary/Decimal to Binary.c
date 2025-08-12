#include <stdio.h>
#include <math.h>

void main() {
    int decimal;
    int binary = 0;

    printf("Enter a Non Negative Integer to be converted to Binary: ");
    scanf("%i", &decimal);

    int temp = decimal;

    for (int i = 0, n = ceil(log(decimal)/log(2)); i < n; i++) {
        binary = binary*10 + temp%2;
        temp /= 2;
    }

    printf("%i is %i in Binary", decimal, binary);
}