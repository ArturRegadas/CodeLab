#include <stdio.h>

int main() {
    int A[7], B[7], C[7][2];
    int i;

    for (i = 0; i < 7; i++) {
        scanf("%d", &A[i]);
    }

    for (i = 0; i < 7; i++) {
        scanf("%d", &B[i]);
    }

    for (i = 0; i < 7; i++) {
        C[i][0] = A[i];
        C[i][1] = B[i];
    }

    for (i = 0; i < 7; i++) {
        printf("%d %d\n", C[i][0], C[i][1]);
    }

    return 0;
}