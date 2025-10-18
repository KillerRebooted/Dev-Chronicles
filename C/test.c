#include<stdio.h>
#include<math.h>
void armstrong(int a)
{
    int n=a,count=0;
    while(n>0)
    {
        n/=10;
        count++;
    }
    int square=a*a;
    if(square%(int)pow(10,count)==a)
    printf("%d is an armstrong number",a);
}
void main()
{
    int a;
    scanf("%d ",&a);
    armstrong(a);
}