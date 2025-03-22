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
int main() {
    int A[20], B[30], C[50];
    
    printf("Digite 20 elementos para a matriz A:\n");
    for (int i = 0; i < 20; i++) {
        printf("A[%d]: ", i);
        scanf("%d", &A[i]);
    }

    printf("\nDigite 30 elementos para a matriz B:\n");
    for (int i = 0; i < 30; i++) {
        printf("B[%d]: ", i);
        scanf("%d", &B[i]);
    }

    for (int i = 0; i < 20; i++) {
        C[i] = A[i];
    }
    for (int i = 0; i < 30; i++) {
        C[20 + i] = B[i];
    }

    mergeSort(C, 0, 49);

    printf("\nElementos da matriz C em ordem decrescente:\n");
    for (int i = 49; i >= 0; i--) {
        printf("%d ", C[i]);
    }

    return 0;
}