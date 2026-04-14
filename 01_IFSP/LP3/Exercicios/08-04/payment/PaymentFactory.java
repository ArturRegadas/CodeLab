package payment;

import payment.Pix;
import payment.CreditCard;
import payment.AuditLog;
import payment.Cripto;

public class PaymentFactory {
    private Pix pix;
    private CreditCard creditCard;
    private AuditLog auditLog;
    private Cripto cripto;

    public PaymentFactory(){
        pix = new Pix();
        creditCard = new CreditCard();
        cripto = new Cripto();
        auditLog = AuditLog.getInstance();
    }

    public void decice(PaymentType choice, double value){
        double ev_value;
        switch (choice){
        case PIX:
            ev_value = pix.pay(value);
            break;
        
        case CREDIT_CARD:
            ev_value = creditCard.pay(value);
            break;
        
        case CRIPTO:
            ev_value = cripto.pay(value);
            break;
        default:
            ev_value = -1;
        }


        auditLog.log(choice, ev_value);
    }
}