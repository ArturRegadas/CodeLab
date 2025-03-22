using System;

class aula4
{
    static int variavelglobal=2;

    static void Main(){

        int variavellocal=1;

        Console.WriteLine(variavellocal);

        Console.WriteLine(variavelglobal);

    }


    void teste(){

        int variavellocal=0;

        Console.WriteLine(variavellocal);

        Console.WriteLine(variavelglobal);

    }
}