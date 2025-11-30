#include <stdio.h>

int main() {
    float real, resultado;
    printf("Digite um número real: ");
    scanf("%f", &real);
    resultado = real / 2.4;
    printf("%.2f\n", resultado);
    return 0;
}
