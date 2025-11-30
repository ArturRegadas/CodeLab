from setup.InitSQLAlchemy import db
class Perfil(db.Model):
    __tablename__ = 'perfis'
    id = db.Column(db.Integer, primary_key=True)
    nome_perfil = db.Column(db.String(80), unique=True, nullable=False)
    usuarios = db.relationship('Usuario', back_populates='perfil')
    def to_dict(self):
        return {"id": self.id, "nome_perfil": self.nome_perfil}
