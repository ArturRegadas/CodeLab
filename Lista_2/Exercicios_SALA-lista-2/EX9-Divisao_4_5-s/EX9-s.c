#include <stdio.h>

int main() {
    int n1, n2, n3;
    scanf("%d", &n1);
    scanf("%d", &n2);
    scanf("%d", &n3);

    if (n1 % 4 == 0) {
        printf("%d é divisível por 4\n", n1);
    }
    if (n1 % 5 == 0) {
        printf("%d é divisível por 5\n", n1);
    }
    if (n2 % 4 == 0) {
        printf("%d é divisível por 4\n", n2);
    }
    if (n2 % 5 == 0) {
        printf("%d é divisível por 5\n", n2);
    }
    if (n3 % 4 == 0) {
        printf("%d é divisível por 4\n", n3);
    }
    if (n3 % 5 == 0) {
        printf("%d é divisível por 5\n", n3);
    }

    return 0;
}
