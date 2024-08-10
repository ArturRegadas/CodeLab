#include <stdio.h>

int main() {
    int n1, n2, n3;
    scanf("%d", &n1);
    scanf("%d", &n2);
    scanf("%d", &n3);

    if (n1 % 2 == 0) {
        printf("%d é divisível por 2\n", n1);
    }
    if (n1 % 3 == 0) {
        printf("%d é divisível por 3\n", n1);
    }
    if (n2 % 2 == 0) {
        printf("%d é divisível por 2\n", n2);
    }
    if (n2 % 3 == 0) {
        printf("%d é divisível por 3\n", n2);
    }
    if (n3 % 2 == 0) {
        printf("%d é divisível por 2\n", n3);
    }
    if (n3 % 3 == 0) {
        printf("%d é divisível por 3\n", n3);
    }

    return 0;
}
