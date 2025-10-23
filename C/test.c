# include <stdio.h>

int main ()
{
    int n , k , protect = 0;
    scanf("%d %d", &n , &k);

    char s[n];
    for (int a = 0 ; a <= n-1 ; a++)
        scanf("%c", &s[a]);
    
    if (s[0] == '1')
        protect++;
    
    for (int i = 1 ; i <= n-1 ; i++)
    {
        int z = i-k+1;

        if (z <= 0)
            z = 0;
        
        if (s[i] == '1')
        {
            int b = 0;
            
            for (int j = i-1 ; j >= z ; j--)
            {
                if (s[j] == '1')
                    b = 1;
            }
            
            if (b == 0)
                protect++;
        }
    }

    printf("%d", protect);
}