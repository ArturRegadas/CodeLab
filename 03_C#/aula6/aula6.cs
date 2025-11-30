using System;

class aula6
{
    static void Main(string[] args)
    {
        int n1,n2,n3;
        
        n1=15;
        n2=20;
        
        Console.WriteLine("A soma entre {0} e {1} e {2}",n1,n2, n1+n2);
        
        double preco, precovenda, pdelucro;
        string produto="Prato Feito";
        preco=9.0;
        pdelucro=1.2;
        
        Console.WriteLine("Produto.......{0,12}",produto);
        Console.WriteLine("Preço.........{0,12:c}",preco);
        Console.WriteLine("Lucro.........{0,12:p}", pdelucro);
        Console.WriteLine("Venda.........{0,12:c}",preco+preco*pdelucro);

    }
}