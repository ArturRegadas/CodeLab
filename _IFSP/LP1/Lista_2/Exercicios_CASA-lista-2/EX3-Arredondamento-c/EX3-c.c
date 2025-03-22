#include <stdio.h>
#include <math.h>

int main() {
    float num;
    scanf("%f", &num);
    if (fmod(num, 1)==0.5){
        num-=0.1;
    }
    printf("%.0f\n", num);
}