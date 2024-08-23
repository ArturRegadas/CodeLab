#include <stdio.h>

int main(){
    int i =1;
    do{
        if (i%2==0){
            printf("%d e par\n", i);
        }
        else{
            printf("%d e impar\n", i);
        }
        ++i;
    }while(i<21);

    return 0;
}