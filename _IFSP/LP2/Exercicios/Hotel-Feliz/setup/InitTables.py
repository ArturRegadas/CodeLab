from setup.InitSQLAlchemy import db
from models.Perfil import Perfil
from models.Usuario import Usuario

def init_tables(app):
    with app.app_context():
        db.create_all() 
        perfis = ["Administrador", "Recepcionista", "Camareira", "Hóspede"]
        for nome in perfis:
            if not Perfil.query.filter_by(nome_perfil=nome).first():
                db.session.add(Perfil(nome_perfil=nome))
        db.session.commit()


        admin_perfil = Perfil.query.filter_by(nome_perfil="Administrador").first()
        if not Usuario.query.filter_by(email="admin@estadafeliz.local").first():
            admin = Usuario(nome_completo="Admin Estada Feliz", email="admin@estadafeliz.local", perfil_id=admin_perfil.id)
            admin.set_senha("admin123")
            db.session.add(admin)
            db.session.commit()
    print("Banco inicializado com perfis e usuário admin (email: admin@estadafeliz.local, senha: admin123)")