using System;

public class aula17
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Array, finalmente");
        //no c# precisa falar que tipo de valor ele possui e a quantidade de valores que ele possui
        
        int[] array =new int[4];
        array[0]=11;
        array[1]=22;
        array[2]=33;
        array[3]=44;
        Console.WriteLine(array[0]);
        
        int[] array2=new int[4]{11,22,33,44};
        Console.WriteLine(array2[0]);
        
        int[] array3={11,22,33,44};
        Console.WriteLine(array3[0]);
        
        string[] cidades ={"RJ", "SP", "BH"};
        Console.WriteLine("{0} {1} {2}",cidades[0], cidades[1], cidades[2]);
        
    }
    
}