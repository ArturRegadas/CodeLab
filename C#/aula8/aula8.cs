using System;

class aula8
{
    static void Main(string[] args)
    {
      double n1,n2;
      string nome;
      
      Console.Write("Primeiro numero: ");
      n1=double.Parse(Console.ReadLine());
      Console.Write("\nSegundo numero: ");
      n2=Convert.ToDouble(Console.ReadLine());
      Console.Write("\nDigite seu nome: ");
      nome=Console.ReadLine();
      
      Console.Write("\nA some que {0} fez entre {1} e {2} = {3}", nome, n1, n2, n1+n2);
        
    }
}