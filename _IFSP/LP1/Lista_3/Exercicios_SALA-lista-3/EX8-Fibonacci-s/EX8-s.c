#include <stdio.h>
int main()
{
    int a = 1;
    int b = 1;
    for (int i = 0; i < 15; i++)
    {
        printf("%d\n", a);
        int apoio = a + b;
        a = b;
        b = apoio;
    }
    return 0;
}