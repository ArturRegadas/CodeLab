from flask import Flask, render_template, request, redirect, session, url_for
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(32)

usuarios = {
    "admin": {
        "senha": "123",
        "perfil": "administrador",
        "nome": "Administrador"
    },
    "joao": {
        "senha": "abc",
        "perfil": "cliente",
        "nome": "João da Silva"
    },
    "maria": {
        "senha": "senha",
        "perfil": "suporte",
        "nome": "Maria Oliveira"
    }
}

@app.route("/")
def home():
    if "usuario" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            session["usuario"] = usuario
            session["perfil"] = usuarios[usuario]["perfil"]
            session["nome"] = usuarios[usuario]["nome"]
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", erro="Usuário ou senha incorretos.")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))

    nome = session["nome"]
    perfil = session["perfil"]

    return render_template("dashboard.html", nome=nome, perfil=perfil)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
