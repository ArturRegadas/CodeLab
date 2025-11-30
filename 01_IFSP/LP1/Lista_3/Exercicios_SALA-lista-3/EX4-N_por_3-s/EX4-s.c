#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    while (n < 250)
    {
        printf("%d\n", n);
        n *= 3;
    }
}