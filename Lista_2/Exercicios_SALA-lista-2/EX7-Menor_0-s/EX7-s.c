// Online C compiler to run C program online
#include <stdio.h>
#include <math.h>

int main() {
    // Write C code here
    int num;
    scanf("%d", &num);
    
    if(num<0){
        num=num*-1;
    }
    printf("%d\n", num);
    return 0;
}