from flask import Blueprint, request, jsonify
from models.Usuario import Usuario
from models.Perfil import Perfil
from models.Hospede import Hospede
from setup.InitSQLAlchemy import db
from Verify import perfil_required
from setup.pagination import paginate_or_all
usuario_bp = Blueprint("usuario", __name__)
@usuario_bp.route("/usuarios", methods=["POST"])
@perfil_required(["Administrador"])
def criar_usuario():
    data = request.json or {}
    nome = data.get("nome_completo")
    email = data.get("email")
    senha = data.get("senha")
    perfil_id = data.get("perfil_id")
    if not (email and senha and perfil_id):
        return jsonify({"error": "email, senha e perfil_id sÃ£o obrigatÃ³rios"}), 400
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"error": "Email jÃ¡ cadastrado"}), 400
    perfil = Perfil.query.get(perfil_id)
    if not perfil:
        return jsonify({"error": "Perfil invÃ¡lido"}), 400
    u = Usuario(nome_completo=nome, email=email, perfil_id=perfil_id)
    u.set_senha(senha)
    db.session.add(u)
    db.session.commit()
    return jsonify(u.to_dict()), 201
@usuario_bp.route("/usuarios", methods=["GET"])
@perfil_required(["Administrador"])
def listar_usuarios():
    res = paginate_or_all(Usuario.query)
    return jsonify(res) if isinstance(res, dict) else jsonify(res)
@usuario_bp.route("/usuarios/<int:user_id>", methods=["PUT"])
@perfil_required(["Administrador"])
def atualizar_usuario(user_id):
    u = Usuario.query.get_or_404(user_id)
    data = request.json or {}
    u.nome_completo = data.get("nome_completo", u.nome_completo)
    new_email = data.get("email")
    if new_email and new_email != u.email:
        if Usuario.query.filter_by(email=new_email).first():
            return jsonify({"error": "Email jÃ¡ em uso"}), 400
        u.email = new_email
    if "senha" in data and data["senha"]:
        u.set_senha(data["senha"])
    if "perfil_id" in data:
        perfil = Perfil.query.get(data["perfil_id"])
        if not perfil:
            return jsonify({"error": "Perfil invÃ¡lido"}), 400
        u.perfil_id = perfil.id
    db.session.commit()
    return jsonify(u.to_dict())
@usuario_bp.route("/usuarios/<int:user_id>", methods=["DELETE"])
@perfil_required(["Administrador"])
def apagar_usuario(user_id):
    u = Usuario.query.get_or_404(user_id)
    db.session.delete(u)
    db.session.commit()
    return jsonify({"message": "UsuÃ¡rio removido"})
@usuario_bp.route("/hospedes", methods=["GET"])
def listar_hospedes():
    res = paginate_or_all(Hospede.query)
    return jsonify(res) if isinstance(res, dict) else jsonify(res)