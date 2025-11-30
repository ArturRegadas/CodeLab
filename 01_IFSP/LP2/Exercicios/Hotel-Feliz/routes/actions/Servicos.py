from flask import Blueprint, request, jsonify
from decimal import Decimal
from models.Servico import Servico
from Verify import perfil_required
from setup.InitSQLAlchemy import db
from setup.pagination import paginate_or_all
servicos_bp = Blueprint("servicos", __name__)
@servicos_bp.route("/servicos", methods=["POST"])
@perfil_required(["Administrador", "Recepcionista"])
def criar_servico():
    data = request.json or {}
    nome = data.get("nome_servico")
    preco = data.get("preco")
    if not (nome and preco):
        return jsonify({"error": "nome_servico e preco obrigatÃ³rios"}), 400
    s = Servico(nome_servico=nome, preco=Decimal(preco))
    db.session.add(s)
    db.session.commit()
    return jsonify(s.to_dict()), 201
@servicos_bp.route("/servicos", methods=["GET"])
def listar_servicos():
    res = paginate_or_all(Servico.query)
    return jsonify(res) if isinstance(res, dict) else jsonify(res)