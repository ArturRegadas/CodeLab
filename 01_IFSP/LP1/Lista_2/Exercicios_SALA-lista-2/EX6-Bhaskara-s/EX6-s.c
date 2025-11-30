// Online C compiler to run C program online
#include <stdio.h>
#include <math.h>

int main() {
    // Write C code here
    float a, b, c, delta, raiz_delta, r1, r2;
    
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);
    
    delta = b*b - 4 * a * c;
    if (delta >=0){
        raiz_delta=pow(delta, 0.5);
        r1 = (-b + raiz_delta) / (2 * a);
        r2 = (-b - raiz_delta) / (2 * a);
        
        if(r1==r2){
            printf("%.2f\n", r1);
        }
        else{
            printf("%.2f e %.2f\n", r1, r2);
        }
    }
    else{
        printf("Não tem solucao\n");
    }
    return 0;
}