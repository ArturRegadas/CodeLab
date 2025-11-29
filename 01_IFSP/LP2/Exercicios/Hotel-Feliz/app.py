from flask import Flask, request, jsonify, session, make_response, render_template
from routes.actions.Cookies import cookies_bp
from routes.actions.Faturas import faturas_bp
from routes.actions.Login import login_bp
from routes.actions.Quarto import quarto_bp
from routes.actions.Reserva import reservas_bp
from routes.actions.Servicos import servicos_bp
from routes.actions.Usuario import usuario_bp
from routes.pages.pages_bp import pages_bp
from setup.InitSQLAlchemy import init_app
from setup.InitTables import init_tables

app = Flask(__name__)

init_app(app)
init_tables(app)

app.register_blueprint(cookies_bp)
app.register_blueprint(faturas_bp)
app.register_blueprint(login_bp)
app.register_blueprint(quarto_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(servicos_bp)
app.register_blueprint(usuario_bp)

app.register_blueprint(pages_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
