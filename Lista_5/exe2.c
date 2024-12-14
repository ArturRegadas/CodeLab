#include <stdio.h>

int binarySearch(int nums[], int numsSize, int target) {
    int left =0;
    int right = numsSize;
    int current;
    int factor =0;
    int previus = -1;
    while(nums[current] != target){
        
        
        current = (right - left)/2+factor;
        
        if(nums[current]<target){
            factor=current;
            left = current;
        }
        else{
            right = current;
        }

        if(current == previus){return -1;}
        previus = current;
    }
    
    return current;
    
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

    int A[8], B[8];
    for(int i =0; i<8; ++i){
        scanf("%d", &A[i]);
    }
    for(int i=0; i<8; i++){
        B[i] = A[i]*5;
    }
    mergeSort(B, 0, 7);

    for(int i =0; i<8; i++){
        printf("%d ", B[i]);
    }
    printf("\n");
    int target;
    scanf("%d", &target);
    printf("%d\n", binarySearch(B,7 ,target));

    
    return 0;
}