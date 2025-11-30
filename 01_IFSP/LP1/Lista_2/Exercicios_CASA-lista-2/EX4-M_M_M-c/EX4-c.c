#include <stdio.h>
#include <limits.h> 

int menor_num(int array[], int tamanho) {
    int i;
    int menor = INT_MAX;
    int indice = -1;

    for (i = 0; i < tamanho; i++) {
        if (array[i] < menor) {
            menor = array[i];
            indice = i;
        }
    }
    return indice;
}

void Sort_feio_Dmais(int array[], int tamanho, int sortedList[]) {
    int i;
    int indice;

    for (i = 0; i < tamanho; i++) {
        indice = menor_num(array, tamanho);
        sortedList[i] = array[indice];
        array[indice] = INT_MAX; 
    }
}

int main() {
    int n1, n2, n3;
    
    scanf("%d", &n1);
    scanf("%d", &n2);
    scanf("%d", &n3);
    
    int list [3]={n1, n2 , n3};
    int sortedList [3];
    Sort_feio_Dmais(list, 3, sortedList);
    
    //Infelizmente Minhas Capacidades só possibilitam fazer um sort desse, de baixo calão, mas... só nao colocar numero muito grande que ta supimpa
    printf("Infelizmente Minhas Capacidades só possibilitam fazer um sort desse, de baixo calão, mas... só nao colocar numero muito grande que ta supimpa\n\n");
    
    printf("o maior número é %d, o menor é %d, e o do meio é %d\n", sortedList[2],sortedList[0],sortedList[1]);
    return 0;
}