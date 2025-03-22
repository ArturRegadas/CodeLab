using System;

public class aula16
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Goto, nao faco ideia do que e");
        
        inicio:
        
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
            case 'a':
                velocidade=850;
                meio="AVIAO";
                break;
            case 'o':
                velocidade=60;
                meio="ONIBUS";
                break;
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
            
            inicio_got:
            Console.Write("Deseja escolher novamente[s/n]: ");
            char gotoesc = char.Parse(Console.ReadLine());
            if(gotoesc=='s' ||gotoesc=='S'){
                Console.Clear();
                goto inicio;
            }
            else if(gotoesc =='n'||gotoesc =='N'){
                Console.Clear();
                Console.Write("Tchau, tchau!");
            }
            else{
                Console.WriteLine("Voce escolheu uma opcao invalida");
                goto inicio_got;
            }
        }
    }
    
}