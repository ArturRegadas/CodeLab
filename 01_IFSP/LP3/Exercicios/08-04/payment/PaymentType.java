package payment;

public enum PaymentType {
    PIX,
    CREDIT_CARD,
    CRIPTO;

    public static PaymentType getByCode(int code) {
        switch (code) {
            case 1:
                return PIX;
            case 2:
                return CREDIT_CARD;
            case 3:
                return CRIPTO;
            default:
                throw new IllegalArgumentException("Invalid PaymentType");
        }
    }
}