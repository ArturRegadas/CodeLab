public class AuditLog{
    private AuditLog instace;

    private AuditLog(){}

    public static AuditLog getInstance(){
        if(instance == null)
            instance = new AuditLog();
        return instace;
    }

    public void log(PaymentType type, double value){
        System.out.printf("Payment: RS: %2f by %s\n", value, type.toString());
    }
}