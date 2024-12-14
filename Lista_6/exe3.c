#include <stdio.h>

int fatorial(int n) {
    if(n<=1){
        return 1;
    }
    return n* fatorial(n-1);
}

int main() {
    int A[10], B[10][3];
    int i;

    for (i = 0; i < 10; i++) {
        scanf("%d", &A[i]);
    }

    for (i = 0; i < 10; i++) {
        B[i][0] = A[i] + 5;
        B[i][1] = fatorial(A[i]);
        B[i][2] = A[i] * A[i];
    }

    for (i = 0; i < 10; i++) {
        printf("%d %d %d\n", B[i][0], B[i][1], B[i][2]);
    }

    return 0;
}
