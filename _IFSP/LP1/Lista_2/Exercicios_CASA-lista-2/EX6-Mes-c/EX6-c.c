// Online C compiler to run C program online
#include <stdio.h>

int main() {
    
    int num;
    scanf("%d", &num);
    char *meses[12] = {"Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        };
    if (1 <= num && num <= 12){
        printf("%s\n", meses[num-1]);
    }
    else{
        printf("Numero Invalido\n");
    }
    
    return 0;
}