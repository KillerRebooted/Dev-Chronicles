#include <stdio.h>

void texting(char digits[]) {

    char alphas[10] = {
        "",     // 0
        "",     // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    };

    printf("%s", digits);
}

void main() {
    texting("229933");
}