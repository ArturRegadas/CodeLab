#include <stdio.h>

int somatorio(int n) {
    return n*(n+1)/2;
}

int main() {
    int n;
    printf("Digite o valor de N: ");
    scanf("%d", &n);
    
    printf("O somatório dos primeiros %d números inteiros é: %d\n", n, somatorio(n));
    return 0;
}

