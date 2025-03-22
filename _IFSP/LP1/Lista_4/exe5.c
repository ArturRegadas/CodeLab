#include <stdio.h>
#define SIZE 5

int main(){
        int A[20], B[30], C[50];
        for(int i=0; i<20; ++i){
            scanf("%d", &A[i]);
        }
        for(int i=0; i<30; ++i){
            scanf("%d", &B[i]);
        }
        for(int i=0; i<20; ++i){
            C[i] = A[i];
        }
        for(int i=20; i<50; ++i){
            C[i] =B[i-20];
        }
        for(int i=0; i<50; ++i){
            printf("%d ", C[i]);
        }
        
}