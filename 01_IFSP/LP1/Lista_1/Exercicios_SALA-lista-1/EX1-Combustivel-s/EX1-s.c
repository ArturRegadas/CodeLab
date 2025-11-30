#include <stdio.h>

int main() {
    float t, v, d, lv;
    scanf("%f", &t);
    scanf("%f", &v);
    d = t * v;
    lv = d / 12;
    printf("%.2f %.2f %.2f %.2f\n", t, v, d, lv);
    return 0;
}
