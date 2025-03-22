#include <stdio.h>

int main() {
    int A[4], B[4], C[4][2];
    int i;

    for (i = 0; i < 4; i++) {
        scanf("%d", &A[i]);
    }

    for (i = 0; i < 4; i++) {
        scanf("%d", &B[i]);
    }

    for (i = 0; i < 4; i++) {
        C[i][0] = A[i] * 2;
        C[i][1] = B[i] - 5;
    }

    for (i = 0; i < 4; i++) {
        printf("%d %d\n", C[i][0], C[i][1]);
    }

    return 0;
}
