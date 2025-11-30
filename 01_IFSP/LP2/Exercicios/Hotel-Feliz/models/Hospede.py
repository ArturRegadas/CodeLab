from setup.InitSQLAlchemy import db
class Hospede(db.Model):
    __tablename__ = 'hospedes'
    id_hospede = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(150), nullable=False)
    documento = db.Column(db.String(50), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    id_usuario_sistema = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    usuario_sistema = db.relationship('Usuario')
    reservas = db.relationship('Reserva', back_populates='hospede_principal')
    def to_dict(self):
        return {
            "id_hospede": self.id_hospede,
            "nome_completo": self.nome_completo,
            "documento": self.documento,
            "telefone": self.telefone,
            "email": self.email,
            "id_usuario_sistema": self.id_usuario_sistema
        }
