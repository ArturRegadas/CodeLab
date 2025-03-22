#include <iostream>
#include <string>
#include <map>// O(log n) deixa o dicionario na ordem que as coisas foram adicionadas
#include <unordered_map> // O(1) deixa em ordem aleatoria


int main(){
    //criando dicionario (map)
    std::map<std::string, int> dicio;//vc associa string e int ao map

    dicio["Artur"]=16;
    dicio["cristovao"]=15;
    dicio["Adalberto"]=76;

    std::cout<<dicio["Artur"]<<"\n";

    std::unordered_map<std::string, int> aledicio;

    for(auto i: dicio){
        std::cout<<i.first<<" "<<i.second<<"\n";
    }
    std::cout<<"\n";

    aledicio["Artur"]=16;
    aledicio["cristovao"]=15;
    aledicio["Adalberto"]=76;

    std::cout<<aledicio["Artur"]<<"\n";
    for(auto i: aledicio){
        std::cout<<i.first<<" "<<i.second<<"\n";
    }
    std::cout<<"\n";


    return 0;
}