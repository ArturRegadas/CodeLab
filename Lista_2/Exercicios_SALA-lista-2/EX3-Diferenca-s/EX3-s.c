#include <stdio.h>

int main() {
    
    int n1, n2;
    scanf("%d", &n1);
    scanf("%d", &n2);
    
    if (n1-n2>=0){
        printf("%d\n",n1-n2);
    }
    else{
        printf("%d\n",n2-n1);
    }
    
    return 0;
    
}