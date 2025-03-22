#include <stdio.h>

int main() {
    float kg, alt, imc;

    scanf("%f", &kg);
    scanf("%f", &alt);
    imc = kg / (alt * alt);
    printf("%.2f\n", imc);
    return 0;
}
