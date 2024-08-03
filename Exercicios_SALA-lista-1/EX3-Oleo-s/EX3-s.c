#include <stdio.h>

int main() {
    float r, a, volume;
    scanf("%f", &r);
    scanf("%f", &a);
    volume = 3.14159 * (r * r) * a;
    printf("%.2f\n", volume);
    return 0;
}