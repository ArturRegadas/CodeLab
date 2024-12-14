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

int main(){

int A[12], B[12], C[12];

for (int i =0; i<12;++i){
    scanf("%d",&A[i]);
}

for (int i =0; i<12;++i){
    scanf("%d",&B[i]);
}

mergeSort(A, 0, 11);
mergeSort(B, 0, 11);

for (int i =0; i<12;++i){
    C[i]=A[i] + B[i];
}

mergeSort(C, 0, 11); 

for (int i =0; i<12;++i){
    printf("%d ",C[i]);
}
printf("\n"); 


return 0;
}