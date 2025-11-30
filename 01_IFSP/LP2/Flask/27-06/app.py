from flask import *

app = Flask(__name__)
app.secret_key = "mykey"
produtos = ["Maça", "Banana", "Laranja"]

usuario = "Artur"
senha = "111"

@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['username']
    password = request.form['password']
    return redirect(url_for('home')) if password == senha else "Senha incorreta <br><a href ='/form'>tentar novamente</a>"

@app.route("/profile")
def profile():
    if  'username' in session:
        return f"<h1>Bem vindo de volta, {session['username']}</h1>"
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
        return "Voce foi deslogado"
    return redirect(url_for("home"))

@app.route("/")
def home():
    return render_template("index.html", logado="username" in session, produtos=produtos)

@app.route("/form")
def form():
    return render_template("login.html")


app.run()