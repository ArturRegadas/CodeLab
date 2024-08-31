#include <stdio.h>
#include <limits.h>

int main() {
    int soma = 0;
    int f1 = 0, f2 = 0, f3 = 0, f4 = 0, f5 = 0;
    int fs1 = 0, fs2 = 0, fs3 = 0, fs4 = 0, fs5 = 0;
    int par = 0, imp = 0;
    int n = 0;
    int maior = INT_MIN;
    int menor = INT_MAX;
    char escolha = 's';

    while (escolha != 'n') {
        int nu;

        printf("Digite um número: ");
        scanf("%d", &nu);
        printf("\n");

        soma += nu;
        n++;

        if (nu > maior) {
            maior = nu;
        }
        if (nu < menor) {
            menor = nu;
        }

        int faixa;
        if (nu < 0) {
            f1++;
            faixa = 1;
            fs1 += nu;
        } else if (0 <= nu && nu < 15) {
            f2++;
            faixa = 2;
            fs2 += nu;
        } else if (15 <= nu && nu < 100) {
            f3++;
            faixa = 3;
            fs3 += nu;
        } else if (nu >= 1000) {
            f4++;
            faixa = 4;
            fs4 += nu;
        } else if (101 <= nu && nu < 1000) {
            f5++;
            faixa = 5;
            fs5 += nu;
        }

        if (nu % 2 == 0) {
            par++;
            printf("O número %d é par\n", nu);
        } else {
            imp++;
            printf("O número %d é ímpar\n", nu);
        }

        printf("O número %d está na faixa %d\n", nu, faixa);

        printf("Continuar [s/n]: ");
        scanf(" %c", &escolha); 
        printf("\n");
    }

    if (n > 0) {
        printf("\nA média foi de %.2f\n", (float)soma / n);
    } else {
        printf("Nenhum número foi inserido.\n");
    }

    printf("O maior número foi %d\n", maior);
    printf("O menor número foi %d\n", menor);
    printf("Ao todo foram:\n");
    printf("Faixa 1: %d, soma: %d\n", f1, fs1);
    printf("Faixa 2: %d, soma: %d\n", f2, fs2);
    printf("Faixa 3: %d, soma: %d\n", f3, fs3);
    printf("Faixa 4: %d, soma: %d\n", f4, fs4);
    printf("Faixa 5: %d, soma: %d\n", f5, fs5);
    printf("Ao todo foram %d números pares e %d números ímpares\n", par, imp);

    return 0;
}
