from flask import Blueprint, render_template, session, jsonify
from models.Reserva import Reserva
from models.Hospede import Hospede
from models.Usuario import Usuario
from Verify import perfil_required
pages_bp = Blueprint("pages",__name__)
@pages_bp.route("/")
def index():
    return render_template("register.html")
@pages_bp.route("/login_page")
def login_page():
    return render_template("login.html")
@pages_bp.route("/register_page")
def register_page():
    return render_template("register.html")
@pages_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@pages_bp.route("/perfis_page")
@perfil_required(["Administrador"])
def perfis_page():
    return render_template("perfis.html")
@pages_bp.route("/usuarios_page")
@perfil_required(["Administrador"])
def usuarios_page():
    return render_template("usuarios.html")
@pages_bp.route("/tipos_quarto_page")
def tipos_quarto_page():
    return render_template("tipos_quarto.html")
@pages_bp.route("/quartos_page")
def quartos_page():
    return render_template("quartos.html")
@pages_bp.route("/hospedes_page")
def hospedes_page():
    return render_template("hospedes.html")
@pages_bp.route("/reservas_page")
def reservas_page():
    return render_template("reservas.html")
@pages_bp.route("/servicos_page")
def servicos_page():
    return render_template("servicos.html")
@pages_bp.route("/faturas_page")
def faturas_page():
    return render_template("faturas.html")
@pages_bp.route("/fatura_page/<int:id_fatura>")
def fatura_page(id_fatura):
    return render_template("fatura.html", id_fatura = id_fatura)
@pages_bp.route('/minhas_reservas')
def minhas_reservas():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "UsuÃ¡rio nÃ£o logado"}), 401
    usuario = Usuario.query.get(user_id)
    if not usuario:
        return jsonify({"error": "UsuÃ¡rio nÃ£o encontrado"}), 404
    hospede = Hospede.query.filter_by(id_usuario_sistema=user_id).first()
    if not hospede:
        reservas = []
    else:
        reservas = Reserva.query.filter_by(id_hospede_principal=hospede.id_hospede).all()
    return render_template('minhas_reservas.html', reservas=reservas)
