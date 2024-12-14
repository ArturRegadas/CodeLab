#include <stdio.h>
#define SIZE 5

int main(){
        int A[SIZE], B[SIZE], C[10];
        for(int i=0; i<SIZE; ++i){
            scanf("%d", &A[i]);
        }
        for(int i=0; i<SIZE; ++i){
            scanf("%d", &B[i]);
        }
        for(int i=0; i<5; ++i){
            C[i] = A[i];
        }
        for(int i=5; i<10; ++i){
            C[i] =B[i-5];
        }
        for(int i=0; i<10; ++i){
            printf("%d ", C[i]);
        }
        
}