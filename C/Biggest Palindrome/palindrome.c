#include <stdio.h>
#include <math.h>

int main() {
	int n = 3;
	int num, temp_num, reversed_num, palindrome;

	for (int i = pow(10, n-1); i < pow(10, n); i++) {
		for (int j = pow(10, n-1); j <= i; j++) {
			num = i*j;
            temp_num = num;
			reversed_num = 0;
			while (temp_num > 0) {
				reversed_num = reversed_num*10 + temp_num%10;
				temp_num /= 10;
			}
			if (num == reversed_num) {
                printf("i: %d, j: %d, num: %d\n", i, j, num);
				palindrome = num;
            }
		}
	}
	printf("The Largest Palindromic Number made from product of %d digit numbers is %d", n, palindrome);
}