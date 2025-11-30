from flask import Blueprint, session, request, jsonify
from models.Usuario import Usuario
from models.Hospede import Hospede
from models.Perfil import Perfil
from setup.InitSQLAlchemy import db
login_bp = Blueprint("login", __name__)
@login_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}
    email = data.get("email")
    senha = data.get("senha")
    if not email or not senha:
        return jsonify({"error": "Email e senha sÃ£o obrigatÃ³rios"}), 400
    user = Usuario.query.filter_by(email=email).first()
    if not user or not user.check_senha(senha):
        return jsonify({"error": "Credenciais invÃ¡lidas"}), 401
    session["user_id"] = user.id
    session["email"] = user.email
    session["perfil"] = user.perfil.nome_perfil if user.perfil else None
    return jsonify({"message": "Logado com sucesso", "user": user.to_dict()})
@login_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logout realizado"})
@login_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    nome = data.get("nome_completo")
    email = data.get("email")
    senha = data.get("senha")
    documento = data.get("documento")
    telefone = data.get("telefone")
    if not nome or not email or not senha or not documento:
        return jsonify({"error": "nome_completo, email, senha e documento sÃ£o obrigatÃ³rios"}), 400
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"error": "Email jÃ¡ cadastrado"}), 400
    perfil = Perfil.query.filter_by(nome_perfil="HÃ³spede").first()
    if not perfil:
        perfil = Perfil(nome_perfil="HÃ³spede")
        db.session.add(perfil)
        db.session.commit()
    usuario = Usuario(
        nome_completo=nome,
        email=email,
        perfil_id=perfil.id
    )
    usuario.set_senha(senha)
    db.session.add(usuario)
    db.session.commit()
    hospede = Hospede(
        nome_completo=nome,
        documento=documento,
        telefone=telefone,
        email=email,
        id_usuario_sistema=usuario.id  
    )
    db.session.add(hospede)
    db.session.commit()
    return jsonify({"message": "UsuÃ¡rio e hÃ³spede criados com sucesso!"}), 201