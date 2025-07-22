from flask import *

app = Flask(__name__)
app.secret_key = "SECRET_KEY_"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    if (username and email and password):
        session["user"] = {}
        session["user"]["username"] = username
        session["user"]["email"] = email
        session["user"]["password"] = password
        flash(f"Usuario {username} foi cadastrado com sucesso", "success")
        return redirect(url_for("home"))
    flash("Todos os campos sao obrigatorios", "danger")
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("home"))


app.run(debug=True)