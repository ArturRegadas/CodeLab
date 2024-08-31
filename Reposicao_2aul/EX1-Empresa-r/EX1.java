import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String nome;
        float sa, ns;
        int pct;

        System.out.print("Funcionário: ");
        nome = scanner.nextLine();

        System.out.print("Salario: ");
        sa = scanner.nextFloat();

        if (sa <= 400.00f) {
            pct = 15;
        } else if (sa <= 700.00f) {
            pct = 12;
        } else if (sa <= 1000.00f) {
            pct = 10;
        } else if (sa <= 1800.00f) {
            pct = 7;
        } else if (sa <= 2500.00f) {
            pct = 4;
        } else {
            pct = 0;
        }

        ns = sa + (sa * pct / 100);

        System.out.println("Nome do funcionário: " + nome);
        System.out.println("% de aumento: " + pct + "%");
        System.out.printf("Salário atual: R$ %.2f%n", sa);
        System.out.printf("Novo salário: R$ %.2f%n", ns);
    }
}
