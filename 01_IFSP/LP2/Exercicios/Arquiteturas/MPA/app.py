from flask import Flask, render_template


app = Flask(__name__)


PILOTOS = [
    {"nome": "Max Verstappen", "equipe": "Red Bull"},
    {"nome": "Lewis Hamilton", "equipe": "Mercedes"},
    {"nome": "Charles Leclerc", "equipe": "Ferrari"}
]


@app.route('/')
def index():
    return render_template('index.html', pilotos=PILOTOS)


@app.route('/piloto/<int:id>')
def piloto(id):
    return render_template('piloto.html', p=PILOTOS[id])


if __name__ == '__main__':
    app.run(debug=True)