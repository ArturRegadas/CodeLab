from setup.InitSQLAlchemy import db

class TipoQuarto(db.Model):
    __tablename__ = 'tipos_quarto'
    id_tipo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_tipo = db.Column(db.String(50), unique=True, nullable=False)
    capacidade_maxima = db.Column(db.Integer, nullable=False)
    preco_diaria_base = db.Column(db.Numeric(10, 2), nullable=False)
    descricao = db.Column(db.Text)

    quartos = db.relationship('Quarto', back_populates='tipo')

    def to_dict(self):
        return {
            "id_tipo": self.id_tipo,
            "nome_tipo": self.nome_tipo,
            "capacidade_maxima": self.capacidade_maxima,
            "preco_diaria_base": str(self.preco_diaria_base),
            "descricao": self.descricao
        }


