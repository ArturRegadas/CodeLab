#include <stdio.h>

int main(){
    char esc;
    int n1, n2;
    esc='e';
    while(esc != 'p'){
        scanf(" %c", &esc);
        if(esc == '+'){
            scanf("%d", &n1);
            scanf("%d", &n2);
            printf("%d\n", n1+n2 );
        }
        else if(esc == '-'){
            scanf("%d", &n1);
            scanf("%d", &n2);
            printf("%d\n", n1-n2 );
        }
        else if(esc == '*'){
            scanf("%d", &n1);
            scanf("%d", &n2);
            printf("%d\n", n1*n2 );
        }
        else if(esc == '/'){
            scanf("%d", &n1);
            scanf("%d", &n2);
            printf("%f\n", (float)n1/n2 );
        }
        else if (esc != 'p'){
            printf("Opcao Invalida\n");
        }
    }
    return 0;
}