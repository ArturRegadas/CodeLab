import java.util.Scanner;
import payment.PaymentFactory;
import payment.PaymentType;

public class Main {
    public static void main(String[] args){
        int choice;
        double value;
        PaymentFactory paymentFactory = new PaymentFactory();
        Scanner scan = new Scanner(System.in);

        System.out.print("Choose a payment method\n1 - PIX\n2 - Credit Card\n3 - Cripto\n: ");

        choice = scan.nextInt();
        PaymentType choiceType = PaymentType.getByCode(choice);

        System.out.print("Choose value: ");
        value = scan.nextDouble();

        paymentFactory.decice(choiceType, value);

    }
    
}