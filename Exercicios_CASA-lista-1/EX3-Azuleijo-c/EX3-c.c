#include <stdio.h>

int main() {
    float alturap, largurap, alturaa, larguraa, R;
    
    scanf("%f", &alturap);
    scanf("%f", &largurap);
    scanf("%f", &alturaa);
    scanf("%f", &larguraa);
    R = (alturap * largurap) / (alturaa * larguraa);
    printf("%.2f\n", R);
    return 0;
}
