using System;

public class Aula12
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Vamo ver se tu e o bonzão");
        Console.WriteLine("Se sua media for maior ou igual a 6 voce esta aprovado, senao, fara recuperacao");
        
        Console.Write("Digite sua primeira nota: ");
        double nota1=double.Parse(Console.ReadLine());
        
        Console.Write("Digite sua segunda nota: ");
        double nota2=double.Parse(Console.ReadLine());
        

        if((nota1+nota2)/2>=6){
            Console.WriteLine("Voce foi aprovado, sua media foi {0}",(nota1+nota2)/2);
        }
        else{
            Console.WriteLine("Voce ficou de recuperacao");
            Console.WriteLine("Se sua nova media for maior ou igual a 5 voce sera aprovado, senao sera reprovado");
            Console.Write("qual foi a nota da prova de recuperacao: ");
            double notarec=double.Parse(Console.ReadLine());

            if((nota1+nota2+notarec)/3>=5){
                Console.WriteLine("Sua media foi {0}, voce foi aprovado", (nota1+nota2+notarec)/3);
            }
            else{
                Console.WriteLine("Sua media foi {0}, voce foi reprovado",(nota1+nota2+notarec)/3);
            }
        }
    }
}