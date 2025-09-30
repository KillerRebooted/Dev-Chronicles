#include <stdio.h>

void main() {
    int n =10;
    int right_most, check;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            right_most = n+i-1;
            for (int t = n-1; t > j; t--) {
                if (n%2==0)
                    check = t;
                else
                    check = t+1;

                if (i == 0)
                    if (j == n-1)
                        break;
                    else
                        right_most -= 1;
                else if (check%2!=0)
                    right_most += (n-i-1)*2 + 1;
                else if (check%2==0)
                    right_most += (i-1)*2 + 1;
            }
            printf("%-3d ", right_most);
        }
        printf("\n");
    }
}