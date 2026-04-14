package payment;
import payment.PaymentStrategy;

public class Cripto implements PaymentStrategy{
    public double pay(double value){
        return value;
    }
}