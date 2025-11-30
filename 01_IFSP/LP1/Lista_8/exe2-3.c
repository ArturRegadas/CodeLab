#include <stdio.h>

float calcular_prestacao(float valor, float taxa, int tempo) {
    return valor + (valor * (taxa / 100) * tempo);
}

int main() {
    float valor, taxa, prestacao;
    int tempo;
    
    printf("Digite o valor: ");
    scanf("%f", &valor);
    printf("Digite a taxa: ");
    scanf("%f", &taxa);
    printf("Digite o tempo: ");
    scanf("%d", &tempo);
    
    prestacao = calcular_prestacao(valor, taxa, tempo);
    
    printf("A prestação em atraso é: %.2f\n", prestacao);
    return 0;
}
