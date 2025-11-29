from setup.InitSQLAlchemy import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)  # id_usuario
    nome_completo = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    perfil_id = db.Column(db.Integer, db.ForeignKey('perfis.id'), nullable=False)

    perfil = db.relationship('Perfil', back_populates='usuarios')

    def set_senha(self, senha_plain):
        self.senha_hash = generate_password_hash(senha_plain)

    def check_senha(self, senha_plain):
        return check_password_hash(self.senha_hash, senha_plain)

    def to_dict(self, include_hash=False):
        d = {
            "id": self.id,
            "nome_completo": self.nome_completo,
            "email": self.email,
            "perfil": self.perfil.nome_perfil if self.perfil else None
        }
        if include_hash:
            d["senha_hash"] = self.senha_hash
        return d


