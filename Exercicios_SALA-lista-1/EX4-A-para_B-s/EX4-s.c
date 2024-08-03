#include <stdio.h>
#include <string.h>

int main() {
    char a[100], b[100], v[100];

    scanf("%s", a);
    scanf("%s", b);
    strcpy(v, a);
    strcpy(a, b);
    strcpy(b, v);
    printf("%s %s\n", a, b);
    return 0;
}