using System;

class Program
{
    static void Main()
    {
        int soma = 0;
        int f1 = 0, f2 = 0, f3 = 0, f4 = 0, f5 = 0;
        int fs1 = 0, fs2 = 0, fs3 = 0, fs4 = 0, fs5 = 0;
        int par = 0, imp = 0;
        int n = 0;
        int maior = int.MinValue;
        int menor = int.MaxValue;
        char escolha = 's';

        while (escolha != 'n')
        {
            Console.Write("Digite um número: ");
            int nu = int.Parse(Console.ReadLine());

            soma += nu;
            n++;

            if (nu > maior)
            {
                maior = nu;
            }
            if (nu < menor)
            {
                menor = nu;
            }

            int faixa;
            if (nu < 0)
            {
                f1++;
                faixa = 1;
                fs1 += nu;
            }
            else if (0 <= nu && nu < 15)
            {
                f2++;
                faixa = 2;
                fs2 += nu;
            }
            else if (15 <= nu && nu < 100)
            {
                f3++;
                faixa = 3;
                fs3 += nu;
            }
            else if (nu >= 1000)
            {
                f4++;
                faixa = 4;
                fs4 += nu;
            }
            else if (101 <= nu && nu < 1000)
            {
                f5++;
                faixa = 5;
                fs5 += nu;
            }
            else
            {
                faixa = 0; 
            }

            if (nu % 2 == 0)
            {
                par++;
                Console.WriteLine($"O número {nu} é par");
            }
            else
            {
                imp++;
                Console.WriteLine($"O número {nu} é ímpar");
            }

            Console.WriteLine($"O número {nu} está na faixa {faixa}");

            Console.Write("Continuar [s/n]: ");
            escolha = Console.ReadKey().KeyChar;
            Console.WriteLine(); // Para criar uma nova linha após o input
        }

        if (n > 0)
        {
            Console.WriteLine($"\nA média foi de {((double)soma / n):F2}");
        }
        else
        {
            Console.WriteLine("Nenhum número foi inserido.");
        }

        Console.WriteLine($"O maior número foi {maior}");
        Console.WriteLine($"O menor número foi {menor}");
        Console.WriteLine("Ao todo foram:");
        Console.WriteLine($"Faixa 1: {f1}, soma: {fs1}");
        Console.WriteLine($"Faixa 2: {f2}, soma: {fs2}");
        Console.WriteLine($"Faixa 3: {f3}, soma: {fs3}");
        Console.WriteLine($"Faixa 4: {f4}, soma: {fs4}");
        Console.WriteLine($"Faixa 5: {f5}, soma: {fs5}");
        Console.WriteLine($"Ao todo foram {par} números pares e {imp} números ímpares");
    }
}
