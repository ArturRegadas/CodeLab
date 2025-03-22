#include <iostream>
#include <string>

int main(){
    std::string name;

    std::cin >> name;
    std::cout << name << "\n"; //lê os caracteres até encontrar um espaço, 
                               //tabulação ou nova linha (\n). Após a leitura,
                               // o caractere de separação (como o espaço ou o 
                               //\n) permanece no buffer.

    std::cin.ignore(); // Ignora o ultimo valor deixado no buffer
                       //no caso o \n

    std::string NameCEspaco;

    std::getline(std::cin, NameCEspaco);// lê todos os caracteres até 
                                        //encontrar uma nova linha (\n), incluindo espaços.
                                        //nao deixa nada no buffer
    std::cout << NameCEspaco << "\n";

    return 0;
}
