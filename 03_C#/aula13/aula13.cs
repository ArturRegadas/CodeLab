using System;

public class Aula12
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Vamos escolher TIMES\n[0]Corinthians\n[1]Sao Paulo\n[3]Palmeiras");
        Console.Write("faça sua escolha: ");
        int escolha=int.Parse(Console.ReadLine());
        if(escolha==0){
            Console.WriteLine("Voce escolheu CORINTHIANS");
        }
        else if(escolha==1){
            Console.WriteLine("Voce escolheu SAO PAULO");
        }
        else if(escolha==2){
            Console.WriteLine("Voce escolhei PALMEIRAS");
        }
        else{
            Console.WriteLine("Voce NAO escolheu uma opcao VALIDA");
        }
    }
}