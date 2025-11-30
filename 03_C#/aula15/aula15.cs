using System;

public class aula15
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Switch case é paia!?");
        
        Console.WriteLine("Vamos fazer uma viajem !!");
        Console.Write("Digite a distancia da viajem [km]: ");
        double distancia=double.Parse(Console.ReadLine());
        Console.Write("Digite o meio de transporte\n[a]Aviao\n[o]Onibus\n[b]Barco\nescolha: ");
        char locomocao=char.Parse(Console.ReadLine());
        //"" string
        //'' char
        double velocidade=0;
        bool escolha_correta=true;
        string meio="";
        switch(locomocao){
            case 'A'
            case 'a':
                velocidade=850;
                meio="AVIAO";
                break;
            case 'O'
            case 'o':
                velocidade=60;
                meio="ONIBUS";
                break;
            case 'B'
            case 'b':
                velocidade=35;
                meio="BARCO";
                break;
            default:
                escolha_correta=false;
                break;
            
        }
        if(escolha_correta){
            double tempo = distancia/velocidade;
            Console.WriteLine("Para andar {0}KM de {1} levara {2:f2}H",distancia,meio,tempo);
        }
        else{
            Console.WriteLine("Voce escolheu a opcao {0}, uma opcao invalida!", locomocao);
        }
    }
    
}