import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int soma = 0;
        int f1 = 0, f2 = 0, f3 = 0, f4 = 0, f5 = 0;
        int fs1 = 0, fs2 = 0, fs3 = 0, fs4 = 0, fs5 = 0;
        int par = 0, imp = 0;
        int n = 0;
        int maior = Integer.MIN_VALUE;
        int menor = Integer.MAX_VALUE;
        char escolha = 's';
        
        Scanner scanner = new Scanner(System.in);

        while (escolha != 'n') {
            System.out.print("Digite um número: ");
            int nu = scanner.nextInt();

            soma += nu;
            n++;

            if (nu > maior) {
                maior = nu;
            }
            if (nu < menor) {
                menor = nu;
            }

            int faixa;
            if (nu < 0) {
                f1++;
                faixa = 1;
                fs1 += nu;
            } else if (0 <= nu && nu < 15) {
                f2++;
                faixa = 2;
                fs2 += nu;
            } else if (15 <= nu && nu < 100) {
                f3++;
                faixa = 3;
                fs3 += nu;
            } else if (nu >= 1000) {
                f4++;
                faixa = 4;
                fs4 += nu;
            } else if (101 <= nu && nu < 1000) {
                f5++;
                faixa = 5;
                fs5 += nu;
            } else {
                faixa = 0;
            }

            if (nu % 2 == 0) {
                par++;
                System.out.println("O número " + nu + " é par");
            } else {
                imp++;
                System.out.println("O número " + nu + " é ímpar");
            }

            System.out.println("O número " + nu + " está na faixa " + faixa);

            System.out.print("Continuar [s/n]: ");
            escolha = scanner.next().charAt(0);
        }

        if (n > 0) {
            System.out.println("\nA média foi de " + String.format("%.2f", (double)soma / n));
        } else {
            System.out.println("Nenhum número foi inserido.");
        }

        System.out.println("O maior número foi " + maior);
        System.out.println("O menor número foi " + menor);
        System.out.println("Ao todo foram:");
        System.out.println("Faixa 1: " + f1 + ", soma: " + fs1);
        System.out.println("Faixa 2: " + f2 + ", soma: " + fs2);
        System.out.println("Faixa 3: " + f3 + ", soma: " + fs3);
        System.out.println("Faixa 4: " + f4 + ", soma: " + fs4);
        System.out.println("Faixa 5: " + f5 + ", soma: " + fs5);
        System.out.println("Ao todo foram " + par + " números pares e " + imp + " números ímpares");
    }
}
