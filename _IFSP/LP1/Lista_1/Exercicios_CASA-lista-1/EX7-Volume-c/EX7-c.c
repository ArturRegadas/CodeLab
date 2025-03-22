#include <stdio.h>

int main() {
    float raio, volume, area;
    float pi = 3.1415926;

    scanf("%f", &raio);
    volume = (4.0 / 3.0) * pi * raio * raio * raio;
    area = 4 * pi * raio * raio;
    printf("%.2f\n", volume);
    printf("%.2f\n", area);
    return 0;
}
