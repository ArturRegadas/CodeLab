#include <stdio.h>
void merge(int array[], int left, int midle, int right)
{
    int li = left;
    int ri = midle + 1;

    int aux[right - left + 1];
    int auxIndex = 0;

    while (li < midle + 1 && ri <= right)
    {
        if (array[li] > array[ri])
        {
            aux[auxIndex] = array[ri];
            ri++;
        }
        else
        {
            aux[auxIndex] = array[li];
            li++;
        }
        auxIndex++;
    }
    while (li < midle + 1)
    {
        aux[auxIndex] = array[li];
        li++;
        auxIndex++;
    }
    while (ri <= right)
    {
        aux[auxIndex] = array[ri];
        ri++;
        auxIndex++;
    }

    int index = 0;
    for (int i = left; i <= right; ++i)
    {
        array[i] = aux[index];
        ++index;
    }
}

void mergeSort(int array[], int leftIndex, int rightIndex)
{

    if (leftIndex < rightIndex)
    {

        int midle = leftIndex + (rightIndex - leftIndex) / 2;

        mergeSort(array, leftIndex, midle);
        mergeSort(array, midle + 1, rightIndex);

        merge(array, leftIndex, midle, rightIndex);
    }
}
int pesquisa(int array[], int size, int target){
    for(int i =0; i<size; i++){
        if (array[i] == target){return i;}
    }
    return -1;
}
int main() {
    int A[30], B[30], procurado, posicao;

    printf("Digite 30 elementos para a matriz A:\n");
    for (int i = 0; i < 30; i++) {
        printf("A[%d]: ", i);
        scanf("%d", &A[i]);
    }

    for (int i = 0; i < 30; i++) {
        B[i] = A[i] * A[i] * A[i];
    }

    printf("Digite o número que deseja pesquisar em B: ");
    scanf("%d", &procurado);

    posicao = pesquisa(B, 30, procurado);
    if (posicao != -1) {
        printf("O número %d foi encontrado na posição %d de B.\n", procurado, posicao);
    } else {
        printf("O número %d não foi encontrado em B.\n", procurado);
    }

    return 0;
}   