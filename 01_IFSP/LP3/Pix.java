public class Pix implements PaymentStrategy{
    public double pay(double value){
        return value*0.9;
    }
}