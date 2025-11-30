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
    int notas[40], procurado, posicao;

    printf("Digite as notas de 40 alunos:\n");
    for (int i = 0; i < 40; i++) {
        printf("Nota[%d]: ", i);
        scanf("%d", &notas[i]);
    }

    mergeSort(notas, 0, 39);

    printf("Digite a nota que deseja pesquisar: ");
    scanf("%d", &procurado);

    posicao = pesquisa(notas, 40, procurado);
    if (posicao != -1) {
        printf("A nota %d foi encontrada na posição %d.\n", procurado, posicao);
    } else {
        printf("A nota %d não foi encontrada.\n", procurado);
    }

    return 0;
}