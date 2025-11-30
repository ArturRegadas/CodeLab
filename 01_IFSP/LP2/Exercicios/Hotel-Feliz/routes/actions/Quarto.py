from flask import Blueprint, request, jsonify, session
from decimal import Decimal
from models.TipoQuarto import TipoQuarto
from models.Quarto import Quarto
from setup.InitSQLAlchemy import db
from Verify import perfil_required
from setup.pagination import paginate_or_all
quarto_bp = Blueprint("quarto", __name__)
@quarto_bp.route("/tipos_quarto", methods=["POST"])
@perfil_required(["Administrador", "Recepcionista"])
def criar_tipo_quarto():
    data = request.json or {}
    nome = data.get("nome_tipo")
    capacidade = data.get("capacidade_maxima")
    preco = data.get("preco_diaria_base")
    if not (nome and capacidade and preco):
        return jsonify({"error": "nome_tipo, capacidade_maxima e preco_diaria_base obrigatÃ³rios"}), 400
    if TipoQuarto.query.filter_by(nome_tipo=nome).first():
        return jsonify({"error": "Tipo de quarto jÃ¡ existe"}), 400
    tq = TipoQuarto(
        nome_tipo=nome,
        capacidade_maxima=int(capacidade),
        preco_diaria_base=Decimal(preco),
        descricao=data.get("descricao")
    )
    db.session.add(tq)
    db.session.commit()
    return jsonify(tq.to_dict()), 201
@quarto_bp.route("/tipos_quarto", methods=["GET"])
def listar_tipos_quarto():
    res = paginate_or_all(TipoQuarto.query)
    return jsonify(res) if isinstance(res, dict) else jsonify(res)
@quarto_bp.route("/quartos", methods=["POST"])
@perfil_required(["Administrador", "Recepcionista"])
def criar_quarto():
    data = request.json or {}
    numero = data.get("numero_quarto")
    id_tipo = data.get("id_tipo")
    if not (numero and id_tipo):
        return jsonify({"error": "numero_quarto e id_tipo obrigatÃ³rios"}), 400
    if Quarto.query.get(numero):
        return jsonify({"error": "Quarto jÃ¡ existe"}), 400
    tipo = TipoQuarto.query.get(id_tipo)
    if not tipo:
        return jsonify({"error": "Tipo invÃ¡lido"}), 400
    q = Quarto(numero_quarto=numero, id_tipo=id_tipo, status_limpeza=data.get("status_limpeza", "Sujo"), localizacao=data.get("localizacao"))
    db.session.add(q)
    db.session.commit()
    return jsonify(q.to_dict()), 201
@quarto_bp.route("/quartos", methods=["GET"])
def listar_quartos():
    res = paginate_or_all(Quarto.query)
    return jsonify(res) if isinstance(res, dict) else jsonify(res)
@quarto_bp.route("/quartos/<numero_quarto>", methods=["PUT"])
@perfil_required(["Administrador", "Recepcionista", "Camareira"])
def atualizar_quarto(numero_quarto):
    q = Quarto.query.get_or_404(numero_quarto)
    data = request.json or {}
    perfil = session.get("perfil")
    if perfil == "Camareira":
        q.status_limpeza = data.get("status_limpeza", q.status_limpeza)
    else:
        q.localizacao = data.get("localizacao", q.localizacao)
        if "id_tipo" in data:
            tipo = TipoQuarto.query.get(data["id_tipo"])
            if not tipo:
                return jsonify({"error": "Tipo invÃ¡lido"}), 400
            q.id_tipo = tipo.id_tipo
        q.status_limpeza = data.get("status_limpeza", q.status_limpeza)
    db.session.commit()
    return jsonify(q.to_dict())
@quarto_bp.route("/quartos/<numero_quarto>", methods=["DELETE"])
@perfil_required(["Administrador"])
def apagar_quarto(numero_quarto):
    q = Quarto.query.get_or_404(numero_quarto)
    db.session.delete(q)
    db.session.commit()
    return jsonify({"message": "Quarto removido"})