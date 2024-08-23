#include <stdio.h>

int main(){
    int x =0; 
    while(x<21){
        if (x%2==0){
            printf("%d e par\n", x);
        }
        else{
            printf("%d e Impar\n", x);
        }
        ++x;
    }
    return 0;
}