#include <stdio.h>

int main() {
    float l1, l2, l3;

    scanf("%f", &l1);
    scanf("%f", &l2);
    scanf("%f", &l3);

    if (l1 < l2 + l3 && l2 < l1 + l3 && l3 < l1 + l2) {
        if (l1 != l2 && l2 != l3 && l1 != l3) {
            printf("É um triângulo Escaleno\n");
        } else if (l1 == l2 && l2 == l3) {
            printf("É um triângulo Equilátero\n");
        } else {
            printf("É um triângulo Isósceles\n");
        }
    } else {
        printf("Não é um triângulo\n");
    }

    return 0;
}
