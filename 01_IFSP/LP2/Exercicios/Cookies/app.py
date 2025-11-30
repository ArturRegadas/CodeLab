from flask import Flask, render_template, request, redirect, session, url_for, make_response
from datetime import datetime, timedelta
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(32)

USUARIO_NOME = "admin"
USUARIO_SENHA = "123"

noticias = {
    "Esportes": [
        {"id": 1, "titulo": "Ponte Preta vence campeonato", "conteudo": "Detalhes completos da notícia de esportes."},
        {"id": 2, "titulo": "Lebron James bate recorde mundial", "conteudo": "Resumo da grande conquista."},
        {"id": 3, "titulo": "Final do Paulista movimenta torcida", "conteudo": "Informações sobre o evento esportivo."}
    ],
    "Entretenimento": [
        {"id": 4, "titulo": "Ratatouille lidera bilheteria", "conteudo": "O grande sucesso do cinema."},
        {"id": 5, "titulo": "Amy Lee lança novo álbum", "conteudo": "Detalhes sobre o lançamento musical."},
        {"id": 6, "titulo": "Stranger Things confirma nova temporada", "conteudo": "O que esperar da continuação?"}
    ],
    "Lazer": [
        {"id": 7, "titulo": "Disney inaugura nova atração", "conteudo": "Diversão garantida para todas as idades."},
        {"id": 8, "titulo": "São Paulo ganha destaque", "conteudo": "Belezas naturais da região."},
        {"id": 9, "titulo": "Fórmula 1 reúne artistas locais", "conteudo": "Evento promete movimentar a cidade."}
    ]
}

@app.route("/", methods=["GET", "POST"])
def login():
    tema = request.cookies.get("tema", "light")

    if request.method == "POST":
        nome = request.form.get("usuario")
        senha = request.form.get("senha")

        if nome == USUARIO_NOME and senha == USUARIO_SENHA:
            session["usuario"] = nome
            session["visitas"] = 0
            session["categoria"] = "Esportes"
            return redirect(url_for("home"))
        else:
            return render_template("login.html", erro="Usuário ou senha incorretos.", tema=tema)

    return render_template("login.html", tema=tema)


@app.route("/home")
def home():
    if "usuario" not in session:
        return redirect(url_for("login"))

    tema = request.cookies.get("tema", "light")

    session["visitas"] += 1
    usuario = session["usuario"]

    categoria = session.get("categoria", "Esportes")
    lista_noticias = noticias[categoria]

    return render_template(
        "home.html",
        usuario=usuario,
        visitas=session["visitas"],
        categoria=categoria,
        noticias=lista_noticias,
        tema=tema
    )


@app.route("/categoria", methods=["POST"])
def categoria():
    nova = request.form.get("categoria")
    session["categoria"] = nova
    return redirect(url_for("home"))


@app.route("/noticia/<int:id>")
def noticia(id):
    if "usuario" not in session:
        return redirect(url_for("login"))

    tema = request.cookies.get("tema", "light")

    for categoria in noticias.values():
        for item in categoria:
            if item["id"] == id:
                return render_template("noticia.html", noticia=item, usuario=session["usuario"], tema=tema)

    return "Notícia não encontrada.", 404



@app.route("/tema/<string:modo>")
def tema(modo):
    resp = make_response(redirect(url_for("home")))
    resp.set_cookie("tema", modo, max_age=300)
    return resp


@app.route("/logout")
def logout():
    session.clear()
    resp = make_response(redirect(url_for("login")))
    resp.delete_cookie("tema")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
