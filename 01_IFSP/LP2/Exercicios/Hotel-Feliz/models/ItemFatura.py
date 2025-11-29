from setup.InitSQLAlchemy import db

class ItemFatura(db.Model):
    __tablename__ = 'itens_fatura'
    id_item = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_fatura = db.Column(db.Integer, db.ForeignKey('faturas.id_fatura'), nullable=False)
    id_servico = db.Column(db.Integer, db.ForeignKey('servicos.id_servico'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    preco_unitario_registro = db.Column(db.Numeric(10, 2), nullable=False)
    data_consumo = db.Column(db.DateTime, nullable=False)

    fatura = db.relationship('Fatura', back_populates='itens')
    servico = db.relationship('Servico', back_populates='itens_fatura')

    def to_dict(self):
        return {
            "id_item": self.id_item,
            "id_fatura": self.id_fatura,
            "id_servico": self.id_servico,
            "nome_servico": self.servico.nome_servico if self.servico else None,
            "quantidade": self.quantidade,
            "preco_unitario_registro": str(self.preco_unitario_registro),
            "data_consumo": self.data_consumo.isoformat()
        }