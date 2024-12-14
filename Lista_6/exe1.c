#include <stdio.h>

int main() {
    int A[5][3], B[5][3], C[5][3];
    int linha, coluna;

    for (linha = 0; linha < 5; linha++) {
        for (coluna = 0; coluna < 3; coluna++) {
            scanf("%d", &A[linha][coluna]);
        }
    }

    for (linha = 0; linha < 5; linha++) {
        for (coluna = 0; coluna < 3; coluna++) {
            scanf("%d", &B[linha][coluna]);
        }
    }

    for (linha = 0; linha < 5; linha++) {
        for (coluna = 0; coluna < 3; coluna++) {
            C[linha][coluna] = A[linha][coluna] + B[linha][coluna];
        }
    }

    for (linha = 0; linha < 5; linha++) {
        for (coluna = 0; coluna < 3; coluna++) {
            printf("%d ", C[linha][coluna]);
        }
        printf("\n");
    }

    return 0;
}
