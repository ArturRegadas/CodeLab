// Online C compiler to run C program online
#include <stdio.h>

int main() {
    float Nhrs, sals, sal, hrs, nsal;
    
    while(1){
        
        scanf("%f", &sal);
        if (sal <=0){
            break;
        }
        scanf("%f", &hrs);
        float salbrut;
        salbrut=sal;
        if (sal>1600){
            nsal = sal - (22 * sal / 100);
        }
        else if (sal >= 800){
            nsal = sal - (13 * sal / 100);
        }
        else{
            nsal = sal;
        }
        if (hrs > 160){
            Nhrs = (salbrut/160)*0.5*(hrs-160);
        }
        else{
            Nhrs = 0;
        }
        sals+=nsal + Nhrs;
        printf("o salário líquido desse funcionário é %.2f\n",nsal + Nhrs);
    }
    printf("o total de salários líquidos foi de %.2f\n", sals);
    
}