#include <stdio.h>

int main() {
    float v, t, te, resultado;
    scanf("%f", &v);
    scanf("%f", &t);
    scanf("%f", &te);
    resultado = v + (v * (te / 100) * t);
    printf("%.2f\n", resultado);
    return 0;
}
