#include <stdio.h>

int main() {
    float n1, n2, n3;
    scanf("%f", &n1);
    scanf("%f", &n2);
    scanf("%f", &n3);
    
    if ((n1 + n2 + n3) / 3 >= 6){
        printf("O aluno foi Aprovado com a média %.2f\n",(n1 + n2 + n3) / 3);
    }
    
    else{
        printf("O aluno foi Reprovado com a média %.2f\n",(n1 + n2 + n3) / 3);
    }
    return 0;
}