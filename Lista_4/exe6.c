#include <stdio.h>
#define SIZE 8

int main(){
        int A[SIZE], B[SIZE];
        for(int i=0; i<SIZE; ++i){
            scanf("%d", &A[i]);
        }
        for(int i=0; i<SIZE; ++i){
            B[i] = A[i]*A[i];
        }
        for(int i=0; i<SIZE; ++i){
            printf("%d ", B[i]);
        }
}