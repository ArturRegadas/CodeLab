public class PaymentStrategy {
    private Pix pix;
    private CreditCard creditCard;
    private AuditLog auditLog;

    PaymentStrategy(){
        pix = new Pix();
        creditCard = new CreditCard();
        auditLog = AuditLog.getInstance();
    }

    public void decice(PaymentType choice, double value) throws Exception{
        switch (choice){
        case PIX:
            pix.pay(value);
            break;
        
        case CREDIT_CARD:
            creditCard.pay(value);
            break;
        }

        auditLog(choice, value);
    }
}