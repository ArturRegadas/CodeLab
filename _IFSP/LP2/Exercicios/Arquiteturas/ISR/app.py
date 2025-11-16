from flask import Flask, send_file
import time, os
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

env = Environment(loader=FileSystemLoader('templates'))

INTERVALO = 60
ULTIMA_GERACAO = 0

    

@app.route('/')
def index():
    global ULTIMA_GERACAO
    if time.time() - ULTIMA_GERACAO > INTERVALO:
        template = env.get_template('index.html')
        html = template.render(
            pilotos=[
                {"nome": "Max Verstappen", "equipe": "Red Bull"},
                {"nome": "Lewis Hamilton", "equipe": "Mercedes"},
                {"nome": "Charles Leclerc", "equipe": "Ferrari"}
            ]
        )
        os.makedirs('dist', exist_ok=True)
        with open('dist/index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        ULTIMA_GERACAO = time.time()
    return send_file('dist/index.html')

if __name__ == '__main__':
    template = env.get_template('index.html')
    html = template.render(pilotos=[{"nome": "Max Verstappen", "equipe": "Red Bull"},
                                   {"nome": "Lewis Hamilton", "equipe": "Mercedes"}])
    os.makedirs('dist', exist_ok=True)
    with open('dist/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    ULTIMA_GERACAO = time.time()
    app.run(debug=True)