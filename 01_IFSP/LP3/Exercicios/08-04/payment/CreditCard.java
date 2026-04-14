package payment;
import payment.PaymentStrategy;
public class CreditCard implements PaymentStrategy{
    public double pay(double value){
        return value;
    }
}