// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int n1, n2, result;
    scanf("%d", &n1);
    scanf("%d", &n2);
    result=n1-n2;
    if (result<0){
        printf("%d\n", result*-1);
    }
    else{
        printf("%d\n", result);
    }
    return 0;
}