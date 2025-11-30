from setup.InitSQLAlchemy import db
class Quarto(db.Model):
    __tablename__ = 'quartos'
    numero_quarto = db.Column(db.String(10), primary_key=True)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipos_quarto.id_tipo'), nullable=False)
    status_limpeza = db.Column(db.String(20), nullable=False, default='Sujo')
    localizacao = db.Column(db.String(50))
    tipo = db.relationship('TipoQuarto', back_populates='quartos')
    reservas = db.relationship('Reserva', back_populates='quarto')
    def to_dict(self):
        return {
            "numero_quarto": self.numero_quarto,
            "id_tipo": self.id_tipo,
            "status_limpeza": self.status_limpeza,
            "localizacao": self.localizacao,
            "tipo": self.tipo.nome_tipo if self.tipo else None
        }
