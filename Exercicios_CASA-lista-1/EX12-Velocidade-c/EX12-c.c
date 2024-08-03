#include <stdio.h>

int main() {
    float metros, hrs, km, resultado;

    scanf("%f", &metros);
    scanf("%f", &hrs);
    km = metros / 1000;
    resultado = km / hrs;
    printf("%.2f\n", resultado);
    return 0;
}
