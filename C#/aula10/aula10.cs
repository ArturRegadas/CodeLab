using System;

public class aula10
{
    enum DiasSemana{Segunda,Terca,Quarta,Quinta,Sexta,Sabado,Domingo};
    public static void Main(string[] args)
    {
        DiasSemana diasemna=(DiasSemana)0;
        Console.WriteLine(diasemna);
        
        int ds=(int)DiasSemana.Segunda;
        Console.WriteLine(ds);

    }
}