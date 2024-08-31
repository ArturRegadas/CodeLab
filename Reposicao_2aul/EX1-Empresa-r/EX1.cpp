#include <iostream>
#include <iomanip>
#include <string>

int main() {
    std::string nome;
    float sa, ns;
    int pct;

    std::cout << "Funcionário: ";
    std::getline(std::cin, nome);
    std::cout << ""<< std::endl;

    std::cout << "Salário: ";
    std::cin >> sa;

    if (sa <= 400.00f) {
        pct = 15;
    } else if (sa <= 700.00f) {
        pct = 12;
    } else if (sa <= 1000.00f) {
        pct = 10;
    } else if (sa <= 1800.00f) {
        pct = 7;
    } else if (sa <= 2500.00f) {
        pct = 4;
    } else {
        pct = 0;
    }

    ns = sa + (sa * pct / 100);
    std::cout << ""<< std::endl;
    std::cout << "Nome do funcionário: " << nome << std::endl;
    std::cout << "% de aumento: " << pct << "%" << std::endl;
    std::cout << "Salário atual: R$ " << std::fixed << std::setprecision(2) << sa << std::endl;
    std::cout << "Novo salário: R$ " << std::fixed << std::setprecision(2) << ns << std::endl;

    return 0;
}
