from setup.InitSQLAlchemy import db

class Servico(db.Model):
    __tablename__ = 'servicos'
    id_servico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_servico = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)

    itens_fatura = db.relationship('ItemFatura', back_populates='servico')

    def to_dict(self):
        return {"id_servico": self.id_servico, "nome_servico": self.nome_servico, "preco": str(self.preco)}


