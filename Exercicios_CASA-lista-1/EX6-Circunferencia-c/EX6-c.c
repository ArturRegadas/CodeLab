#include <stdio.h>

int main() {
    float raio, area, circunferencia;
    const float pi = 3.1415926;

    scanf("%f", &raio);
    area = pi * raio * raio;
    circunferencia = 2 * pi * raio;
    printf("%.2f\n", area);
    printf("%.2f\n", circunferencia);
    return 0;
}
