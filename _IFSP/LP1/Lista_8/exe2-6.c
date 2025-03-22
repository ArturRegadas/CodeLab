#include <stdio.h>

int fibonacci(int n) {
    if (n<=1){
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int n;
    
    printf("Digite o número de termos da sequência de Fibonacci: ");
    scanf("%d", &n);
    
    int re = fibonacci(n);
    
    return 0;
}
