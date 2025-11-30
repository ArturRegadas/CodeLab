#include <stdio.h>
#define SIZE 5

int main(){
        int A[SIZE], B[SIZE], C[SIZE];
        for(int i=0; i<SIZE; ++i){
            scanf("%d", &A[i]);
        }
        for(int i=0; i<SIZE; ++i){
            scanf("%d", &B[i]);
        }
        for(int i=0; i<SIZE; ++i){
            C[i] = A[i] - B[i];
        }
        for(int i=0; i<SIZE; ++i){
            printf("%d ", C[i]);
        }
}