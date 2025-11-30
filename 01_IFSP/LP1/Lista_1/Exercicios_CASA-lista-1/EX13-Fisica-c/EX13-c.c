#include <stdio.h>

int main() {
    float t, resultado;

    scanf("%f", &t);
    resultado = 2 + 3 * t + 0.5 * 10 * t * t;
    printf("%.2f\n", resultado);
    return 0;
}
