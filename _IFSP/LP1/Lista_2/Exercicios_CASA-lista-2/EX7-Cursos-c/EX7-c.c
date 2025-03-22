#include <stdio.h>

int main() {
    
    int num;
    scanf("%d", &num);
    char *meses[12] = {"Engenharia","Edificações","Sistemas Elétricos","Turismo","Análise de Sistemas"};
    if (1 <= num && num <= 5){
        printf("%s\n", meses[num-1]);
    }
    else{
        printf("Numero Invalido\n");
    }
    
    return 0;
}