#include <stdio.h>

int main() {
    float l1, l2, a, p;

    scanf("%f", &l1);
    scanf("%f", &l2);
    a = l1 * l2;
    p = l1 * 2 + l2 * 2;
    printf("Área: %.2f\n", a);
    printf("Perímetro: %.2f\n", p);
    return 0;
}
