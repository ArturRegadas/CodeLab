package payment;
public class AuditLog{
    private static AuditLog instance;

    private AuditLog(){}

    public static AuditLog getInstance(){
        if(instance == null)
            instance = new AuditLog();
        return instance;
    }

    public void log(PaymentType type, double value){
        System.out.printf("Payment: RS: %.2f by %s\n", value, type.toString());
    }
}