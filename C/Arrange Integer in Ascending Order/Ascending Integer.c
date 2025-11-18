#include <stdio.h>

void main() {
    int n, temp_n;
    printf("Input a Number: ");
    scanf("%d", &n);

    printf("\n");

    while (n>0) {
        temp_n = n;
        
        int digit = temp_n%10;
        int smallest_digit = 9;
        while (temp_n>0) {
            digit = temp_n%10;
            if (digit<smallest_digit)
                smallest_digit = digit;
            temp_n/=10;
        }

        printf("%d", smallest_digit);
        
        temp_n = n;
        n = 0;

        while (temp_n>0) {
            digit = temp_n%10;
            if (smallest_digit!=digit)
                n = 10*n + digit;
            else
                smallest_digit = 10;
            temp_n/=10;
        }
    }

}