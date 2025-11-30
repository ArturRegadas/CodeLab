from setup.InitSQLAlchemy import db
class Reserva(db.Model):
    __tablename__ = 'reservas'
    id_reserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_hospede_principal = db.Column(db.Integer, db.ForeignKey('hospedes.id_hospede'), nullable=False)
    numero_quarto = db.Column(db.String(10), db.ForeignKey('quartos.numero_quarto'), nullable=True)
    data_checkin = db.Column(db.Date, nullable=False)
    data_checkout = db.Column(db.Date, nullable=False)
    status_reserva = db.Column(db.String(30), nullable=False, default='Pendente')
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)
    hospede_principal = db.relationship('Hospede', back_populates='reservas')
    quarto = db.relationship('Quarto', back_populates='reservas')
    fatura = db.relationship('Fatura', back_populates='reserva', uselist=False)
    def to_dict(self):
        return {
            "id_reserva": self.id_reserva,
            "id_hospede_principal": self.id_hospede_principal,
            "numero_quarto": self.numero_quarto,
            "data_checkin": self.data_checkin.isoformat(),
            "data_checkout": self.data_checkout.isoformat(),
            "status_reserva": self.status_reserva,
            "valor_total": str(self.valor_total)
        }
