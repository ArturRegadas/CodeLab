#include <iostream>
#include <limits>
#include <iomanip>

int main() {
    int soma = 0;
    int f1 = 0, f2 = 0, f3 = 0, f4 = 0, f5 = 0;
    int fs1 = 0, fs2 = 0, fs3 = 0, fs4 = 0, fs5 = 0;
    int par = 0, imp = 0;
    int n = 0;
    int maior = std::numeric_limits<int>::min();
    int menor = std::numeric_limits<int>::max();
    char escolha = 's';

    while (escolha != 'n') {
        int nu;

        std::cout << "Digite um número: ";
        std::cin >> nu;
        std::cout<<"\n";

        soma += nu;
        n++;

        if (nu > maior) {
            maior = nu;
        }
        if (nu < menor) {
            menor = nu;
        }

        int faixa;
        if (nu < 0) {
            f1++;
            faixa = 1;
            fs1 += nu;
        } else if (0 <= nu && nu < 15) {
            f2++;
            faixa = 2;
            fs2 += nu;
        } else if (15 <= nu && nu < 100) {
            f3++;
            faixa = 3;
            fs3 += nu;
        } else if (nu >= 1000) {
            f4++;
            faixa = 4;
            fs4 += nu;
        } else if (101 <= nu && nu < 1000) {
            f5++;
            faixa = 5;
            fs5 += nu;
        }

        if (nu % 2 == 0) {
            par++;
            std::cout << "O número " << nu << " é par\n";
        } else {
            imp++;
            std::cout << "O número " << nu << " é ímpar\n";
        }

        std::cout << "O número " << nu << " está na faixa " << faixa << "\n";

        std::cout << "Continuar [s/n]: ";
        std::cin >> escolha;
        std::cout<<"\n";
    }

    if (n > 0) {
        std::cout << "\nA média foi de " << std::fixed << std::setprecision(2) << (static_cast<float>(soma) / n) << "\n";
    } else {
        std::cout << "Nenhum número foi inserido.\n";
    }

    std::cout << "O maior número foi " << maior << "\n";
    std::cout << "O menor número foi " << menor << "\n";
    std::cout << "Ao todo foram:\n";
    std::cout << "Faixa 1: " << f1 << ", soma: " << fs1 << "\n";
    std::cout << "Faixa 2: " << f2 << ", soma: " << fs2 << "\n";
    std::cout << "Faixa 3: " << f3 << ", soma: " << fs3 << "\n";
    std::cout << "Faixa 4: " << f4 << ", soma: " << fs4 << "\n";
    std::cout << "Faixa 5: " << f5 << ", soma: " << fs5 << "\n";
    std::cout << "Ao todo foram " << par << " números pares e " << imp << " números ímpares\n";

    return 0;
}
