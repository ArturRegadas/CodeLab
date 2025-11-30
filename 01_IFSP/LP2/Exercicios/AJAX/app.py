from flask import Flask, render_template, session, request, jsonify, redirect, url_for
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(32)


def init_session():
    if "usuarios" not in session:
        session["usuarios"] = []


@app.route("/")
def home():
    return redirect(url_for("dashboard"))


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/api/register", methods=["POST"])
def register():
    init_session()

    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    for user in session["usuarios"]:
        if user["email"] == email:
            return jsonify({"status": "error", "message": "E-mail já cadastrado!"})


    session["usuarios"].append({
        "username": username,
        "email": email,
        "password": password
    })

    session.modified = True

    return jsonify({"status": "success", "message": "Cadastro realizado com sucesso!"})


@app.route("/api/login", methods=["POST"])
def login():
    init_session()

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    for user in session["usuarios"]:
        if user["email"] == email and user["password"] == password:
            session["logged_user"] = user["username"]
            session.modified = True
            return jsonify({
                "status": "success",
                "message": "Login realizado!",
                "redirect": "/dashboard"
            })

    return jsonify({"status": "error", "message": "Credenciais inválidas"})


@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("logged_user", None)
    session.modified = True
    return jsonify({"status": "success", "message": "Logout efetuado!"})


@app.route("/dashboard")
def dashboard():
    if "logged_user" not in session:
        return redirect(url_for("login_page"))

    return render_template("dashboard.html", nome=session["logged_user"])


if __name__ == "__main__":
    app.run(debug=True)
