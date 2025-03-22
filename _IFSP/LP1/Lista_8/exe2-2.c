#include <stdio.h>

void ler_matriz(int matriz[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("Digite o valor do elemento %d: ", i + 1);
        scanf("%d", &matriz[i]);
    }
}

void juntar_matrizes(int A[], int B[], int C[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        C[i] = A[i];
        C[i + tamanho] = B[i];
    }
}

void exibir_matriz(int matriz[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", matriz[i]);
    }
    printf("\n");
}

int main() {
    int A[30], B[30], C[60];
    
    printf("Digite os elementos da matriz A:\n");
    ler_matriz(A, 30);
    
    printf("Digite os elementos da matriz B:\n");
    ler_matriz(B, 30);
    
    juntar_matrizes(A, B, C, 30);
    
    printf("Matriz C (junção de A e B):\n");
    exibir_matriz(C, 60);
    
    return 0;
}
