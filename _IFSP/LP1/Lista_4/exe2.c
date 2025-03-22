#include <stdio.h>

int fact(int num){
    if (num == 1){
        return 1;
    }
    return num * fact(num-1);
}

int main(){
        int A[6], B[6];
        for(int i=0; i<6; ++i){
            scanf("%d", &A[i]);
        }
        for(int i=0; i<6; ++i){
            B[i] = fact(A[i]);
        }
        for(int i=0; i<6; ++i){
            printf("%d ", B[i]);
        }
}