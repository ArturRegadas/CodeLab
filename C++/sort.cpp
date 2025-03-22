#include <iostream>
#include <vector>
#include <string>
#include <algorithm>//poder usar o std::sort


int main(){
    std::vector<int> numeros= {1,5,2,5,1,3,2};

    std::sort(numeros.begin(), numeros.end());

    for(int i : numeros){
        std::cout<<i<<" ";
    }
    //sort descrescente:
    std::sort(numeros.begin(), numeros.end(), std::greater<int>());
    std::cout<<"\n";

    std::vector<std::string> caract={"bh", "al", "dr", "ab"};
    std::sort(caract.begin(), caract.end());
    for(std::string i : caract){
        std::cout<<i<<" ";
    }






    return 0;
}