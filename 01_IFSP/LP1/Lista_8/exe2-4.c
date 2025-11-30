#include <stdio.h>

int calcular_potencia(int base, int exp) {
    int resultado = 1;
    for (int i = 0; i < exp; i++) {
        resultado *= base;
    }
    return resultado;
}

int main() {
    int base, exp;
    
    printf("Digite a base: ");
    scanf("%d", &base);
    printf("Digite o expoente: ");
    scanf("%d", &exp);
    
    printf("%d elevado a %d é: %d\n", base, exp, calcular_potencia(base, exp));
    return 0;
}
