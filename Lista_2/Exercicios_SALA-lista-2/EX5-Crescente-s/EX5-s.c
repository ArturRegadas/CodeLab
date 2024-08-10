#include <stdio.h>
#include <limits.h> 

int menor_num(float array[], int tamanho) {
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

void Sort_feio_Dmais(float array[], int tamanho, float sortedList[]) {
    int i;
    int indice;

    for (i = 0; i < tamanho; i++) {
        indice = menor_num(array, tamanho);
        sortedList[i] = array[indice];
        array[indice] = INT_MAX; 
    }
}


int main() {
    //Infelizmente Minhas Capacidades só possibilitam fazer um sort desse, de baixo calão, mas... só nao colocar numero muito grande que ta supimpa
    printf("Infelizmente Minhas Capacidades só possibilitam fazer um sort desse, de baixo calão, mas... só nao colocar numero muito grande que ta supimpa\n\n");
    float n1, n2, n3;
    scanf("%f", &n1);
    scanf("%f", &n2);
    scanf("%f", &n3);
    
    float list [3]= {n1, n2, n3};
    float sortedList [3]={n1, n2, n3};
    
    Sort_feio_Dmais(list, 3, sortedList);
    printf("%f\n", sortedList[0]);
    printf("%f\n", sortedList[1]);
    printf("%f\n", sortedList[2]);
    return 0;
}
