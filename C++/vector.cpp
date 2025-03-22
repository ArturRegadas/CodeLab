#include <iostream>
#include <vector>



int main(){
    std::vector<int> numdinamic(10, 1);//cria um vetor com 10 elemntos, todos elementos são 1

    numdinamic.push_back(3);//adiciona ao final
    numdinamic.insert(numdinamic.begin()+0, 26);//insere no indice 0 o valor 26

    for(int i =0; i<numdinamic.size(); i++){
        std::cout<<numdinamic[i]<<" ";
    }
    std::cout<<"\n";

    numdinamic.pop_back();//remove o ultimo elemnento do vetor




    for(int onu : numdinamic){
        std::cout<<onu<<" ";
    }




    std::vector<int> novov;//cria novo vetor fazio
    novov.swap(numdinamic);//troca o conteudo do vetor de forma O(1)

    std::cout<<"\n";
    for(int i =0; i<novov.size(); i++){
        std::cout<<novov[i]<<" ";
    }

    //criar subvetor
    //no c++ tem usar itinerador com begin e end
    std::vector<int> subvector(novov.begin()+2, novov.end());//pega do valor 2 em diante

    std::cout<<"\nsubvector:\n";
    for(int i =0; i<subvector.size(); i++){
        std::cout<<subvector[i]<<" ";
    }

    numdinamic.clear();//remove todos os elementos do vetor

    return 0;

}