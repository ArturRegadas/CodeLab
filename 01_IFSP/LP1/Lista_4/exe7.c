#include <stdio.h>
#define SIZE 10

int main(){
        int A[SIZE], B[SIZE];
        for(int i=0; i<SIZE; ++i){
            scanf("%d", &A[i]);
        }
        for(int i = 9; i>=0; i--){
            B[9-i] = A[i];
            printf("%d %d \n", 9-i, i);
        }
        for(int i=0; i<SIZE; ++i){
            printf("%d ", B[i]);
        }
}