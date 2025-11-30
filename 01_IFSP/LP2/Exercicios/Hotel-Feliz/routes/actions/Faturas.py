from flask import Blueprint, request, jsonify
from decimal import Decimal
from Verify import perfil_required
from models.Reserva import Reserva
from models.Fatura import Fatura
from models.Servico import Servico
from models.ItemFatura import ItemFatura
from setup.InitSQLAlchemy import db
from setup.pagination import paginate_or_all
faturas_bp = Blueprint("faturas", __name__)
@faturas_bp.route("/faturas", methods=["POST"])
@perfil_required(["Administrador", "Recepcionista"])
def criar_fatura():
    data = request.json or {}
    id_reserva = data.get("id_reserva")
    if not id_reserva:
        return jsonify({"error": "id_reserva obrigatÃ³rio"}), 400
    reserva = Reserva.query.get(id_reserva)
    if not reserva:
        return jsonify({"error": "Reserva nÃ£o encontrada"}), 404
    dias = (reserva.data_checkout - reserva.data_checkin).days
    valor_diarias = Decimal(reserva.quarto.tipo.preco_diaria_base) * dias if reserva.quarto else Decimal("0.00")
    f = Fatura(id_reserva=id_reserva, valor_servicos=Decimal("0.00"), valor_diarias=valor_diarias, status_pagamento=data.get("status_pagamento","Pendente"))
    db.session.add(f)
    db.session.commit()
    return jsonify(f.to_dict()), 201
@faturas_bp.route("/faturas/<int:id_fatura>/itens", methods=["POST"])
@perfil_required(["Administrador", "Recepcionista"])
def adicionar_item_fatura(id_fatura):
    f = Fatura.query.get_or_404(id_fatura)
    data = request.json or {}
    id_servico = data.get("id_servico")
    quantidade = int(data.get("quantidade", 1))
    servico = Servico.query.get(id_servico)
    if not servico:
        return jsonify({"error": "ServiÃ§o invÃ¡lido"}), 400
    preco_unit = Decimal(servico.preco)
    item = ItemFatura(id_fatura=id_fatura, id_servico=id_servico, quantidade=quantidade, preco_unitario_registro=preco_unit, data_consumo=datetime.utcnow())
    db.session.add(item)
    f.valor_servicos = (f.valor_servicos or Decimal("0.00")) + preco_unit * quantidade
    db.session.commit()
    return jsonify(item.to_dict()), 201
@faturas_bp.route("/faturas/<int:id_fatura>", methods=["GET"])
def ver_fatura(id_fatura):
    f = Fatura.query.get_or_404(id_fatura)
    return jsonify(f.to_dict())
@faturas_bp.route("/faturas", methods=["GET"])
def listar_faturas():
    res = paginate_or_all(Fatura.query)
    return jsonify(res) if isinstance(res, dict) else jsonify(res)