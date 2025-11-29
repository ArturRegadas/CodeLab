from flask import Blueprint, request, jsonify
from decimal import Decimal
from datetime import datetime
from models.Hospede import Hospede
from models.Reserva import Reserva
from models.Quarto import Quarto
from setup.InitSQLAlchemy import db
from Verify import perfil_required

reservas_bp = Blueprint("reservas", __name__)

@reservas_bp.route("/reservas", methods=["POST"])
@perfil_required(["Administrador", "Recepcionista"])
def criar_reserva():
    data = request.json or {}
    id_hospede = data.get("id_hospede_principal")
    checkin = data.get("data_checkin")
    checkout = data.get("data_checkout")
    numero_quarto = data.get("numero_quarto") 
    if not (id_hospede and checkin and checkout):
        return jsonify({"error": "id_hospede_principal, data_checkin e data_checkout obrigatórios"}), 400

    
    try:
        dt_checkin = datetime.fromisoformat(checkin).date()
        dt_checkout = datetime.fromisoformat(checkout).date()
    except Exception:
        return jsonify({"error": "Formato de data inválido. Use YYYY-MM-DD"}), 400
    if dt_checkout <= dt_checkin:
        return jsonify({"error": "data_checkout deve ser posterior a data_checkin"}), 400

    hosp = Hospede.query.get(id_hospede)
    if not hosp:
        return jsonify({"error": "Hóspede não encontrado"}), 404

    
    valor_total = Decimal("0.00")
    if numero_quarto:
        quarto = Quarto.query.get(numero_quarto)
        if not quarto:
            return jsonify({"error": "Quarto não encontrado"}), 404
        dias = (dt_checkout - dt_checkin).days
        valor_total = Decimal(quarto.tipo.preco_diaria_base) * dias

    r = Reserva(
        id_hospede_principal=id_hospede,
        numero_quarto=numero_quarto,
        data_checkin=dt_checkin,
        data_checkout=dt_checkout,
        status_reserva=data.get("status_reserva", "Pendente"),
        valor_total=valor_total
    )
    db.session.add(r)
    db.session.commit()
    return jsonify(r.to_dict()), 201


@reservas_bp.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([r.to_dict() for r in reservas])


@reservas_bp.route("/reservas/<int:id_reserva>", methods=["PUT"])
@perfil_required(["Administrador", "Recepcionista"])
def atualizar_reserva(id_reserva):
    r = Reserva.query.get_or_404(id_reserva)
    data = request.json or {}
    if "numero_quarto" in data:
        if data["numero_quarto"] is not None:
            q = Quarto.query.get(data["numero_quarto"])
            if not q:
                return jsonify({"error": "Quarto inválido"}), 400
        r.numero_quarto = data["numero_quarto"]
    if "status_reserva" in data:
        r.status_reserva = data["status_reserva"]
    
    if "data_checkin" in data:
        r.data_checkin = datetime.fromisoformat(data["data_checkin"]).date()
    if "data_checkout" in data:
        r.data_checkout = datetime.fromisoformat(data["data_checkout"]).date()

    if r.numero_quarto:
        dias = (r.data_checkout - r.data_checkin).days
        r.valor_total = Decimal(r.quarto.tipo.preco_diaria_base) * dias
    db.session.commit()
    return jsonify(r.to_dict())


@reservas_bp.route("/reservas/<int:id_reserva>", methods=["DELETE"])
@perfil_required(["Administrador"])
def apagar_reserva(id_reserva):
    r = Reserva.query.get_or_404(id_reserva)
    db.session.delete(r)
    db.session.commit()
    return jsonify({"message": "Reserva removida"})

