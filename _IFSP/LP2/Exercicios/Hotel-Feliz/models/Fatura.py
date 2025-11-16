
from setup.InitSQLAlchemy import db
from datetime import datetime

class Fatura(db.Model):
    __tablename__ = 'faturas'
    id_fatura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_reserva = db.Column(db.Integer, db.ForeignKey('reservas.id_reserva'), nullable=False)
    data_emissao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    valor_servicos = db.Column(db.Numeric(10, 2), nullable=False)
    valor_diarias = db.Column(db.Numeric(10, 2), nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False, default='Pendente')

    reserva = db.relationship('Reserva', back_populates='fatura')
    itens = db.relationship('ItemFatura', back_populates='fatura')

    def to_dict(self):
        return {
            "id_fatura": self.id_fatura,
            "id_reserva": self.id_reserva,
            "data_emissao": self.data_emissao.isoformat(),
            "valor_servicos": str(self.valor_servicos),
            "valor_diarias": str(self.valor_diarias),
            "status_pagamento": self.status_pagamento,
            "itens": [i.to_dict() for i in self.itens]
        }


