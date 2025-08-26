#include <stdio.h>
#include <math.h>

void main() {
    int decimal;
    float binary = 0;

    printf("Enter a Non Negative Integer to be converted to Binary: ");
    scanf("%i", &decimal);

    int temp = decimal;

    int n = ceil(log(decimal)/log(2));
    for (int i = 0; i < n+1; i++) {
        binary = binary/10 + temp%2;
        temp /= 2;
    }

    printf("%i is %i in Binary", decimal, (int)(binary*pow(10, n-1)));
}