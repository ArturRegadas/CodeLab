#include <stdio.h>

int main() {
    
    float n1, n2, n3;
    
    scanf("%f", &n1);
    scanf("%f", &n2);
    if ((n1 + n2) / 2 < 6){
        scanf("%f", &n3);
        if ((n1 + n2 + n3) / 3 < 5){
            printf("O aluno foi Reprovado com a média %.2f",(n1 + n2 + n3) / 3);
            }
        else{
            printf("O aluno foi Aprovado com a média %.2f",(n1 + n2 + n3) / 3);
        }
    }
    else{
        printf("O aluno foi Aprovado com a média %.2f",(n1 + n2 ) / 2);
    }
    
    return 0;
    
}