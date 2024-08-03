#include <stdio.h>

int main() {
    float nota1, nota2, nota3, nota4, media_final;

    scanf("%f", &nota1);
    scanf("%f", &nota2);
    scanf("%f", &nota3);
    scanf("%f", &nota4);
    media_final = (nota1 + nota2 + nota3 + nota4) / 4;
    printf("%.2f\n", media_final);
    return 0;
}
