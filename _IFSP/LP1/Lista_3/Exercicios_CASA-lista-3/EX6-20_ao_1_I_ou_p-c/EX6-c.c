#include <stdio.h>

int main(){
    for(int i = 20; i>0; i--){
        if (i%2==0){
            printf("%d e par\n", i);
        }
        else{
            printf("%d e impar\n", i);
        }
    }
    return 0;
    
}