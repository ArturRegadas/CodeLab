#include <stdio.h>

int main() {
    float pr1, pr2, atv, resultado;

    scanf("%f", &pr1);
    scanf("%f", &pr2);
    scanf("%f", &atv);
    resultado = (pr1 * 4 + pr2 * 4 + atv * 2) / 10;
    printf("%.2f\n", resultado);
    return 0;
}
