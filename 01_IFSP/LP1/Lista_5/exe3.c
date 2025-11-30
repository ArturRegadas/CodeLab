#include <stdio.h>

int fact(int num){
    if (num == 1){
        return 1;
    }
    return num * fact(num-1);
}

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

int main(){
    int A[12], B[12];

    for(int i =0; i<12; i++){
        scanf("%d", &A[i]);
    }
    for(int i =0; i<12; i++){
        B[i] = fact(A[i]);
    }

    mergeSort(B, 0, 11);

    for(int i =0; i<12; i++){
        printf("%d ", B[i]);
    }

    printf("\n");

    return 0;
}