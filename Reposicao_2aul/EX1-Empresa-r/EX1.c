#include <stdio.h>

int main() {
    char nome[50];
    float sa, ns;
    int pct;

    printf("Funcionário: ");
    scanf("%s", nome);

    printf("Salario: ");
    scanf("%f", &sa);

    if (sa <= 400.00) {
        pct = 15;
    } else if (sa <= 700.00) {
        pct = 12;
    } else if (sa <= 1000.00) {
        pct = 10;
    } else if (sa <= 1800.00) {
        pct = 7;
    } else if (sa <= 2500.00) {
        pct = 4;
    } else {
        pct = 0;
    }

    ns = sa + (sa * pct / 100);

    printf("\nNome do funcionário: %s\n", nome);
    printf("%% de aumento: %d%%\n", pct);
    printf("Salário atual: R$ %.2f\n", sa);
    printf("Novo salário: R$ %.2f\n", ns);

    return 0;
}
