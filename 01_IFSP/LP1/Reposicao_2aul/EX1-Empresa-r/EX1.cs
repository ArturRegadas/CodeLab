using System;

class Program
{
    static void Main()
    {
        string nome;
        float sa, ns;
        int pct;

        Console.Write("Funcionário: ");
        nome = Console.ReadLine();

        Console.Write("Salario: ");
        sa = float.Parse(Console.ReadLine());

        if (sa <= 400.00f)
        {
            pct = 15;
        }
        else if (sa <= 700.00f)
        {
            pct = 12;
        }
        else if (sa <= 1000.00f)
        {
            pct = 10;
        }
        else if (sa <= 1800.00f)
        {
            pct = 7;
        }
        else if (sa <= 2500.00f)
        {
            pct = 4;
        }
        else
        {
            pct = 0;
        }

        ns = sa + (sa * pct / 100);

        Console.WriteLine($"Nome do funcionário: {nome}");
        Console.WriteLine($"% de aumento: {pct}%");
        Console.WriteLine($"Salário atual: R$ {sa:F2}");
        Console.WriteLine($"Novo salário: R$ {ns:F2}");
    }
}
