from flask import *
from games.hagmanGame import HangmanState
from games.hanoiGame import HanoiState
from games.jokenpoGame import JokenpoState
from games.navalGame import NavalGameState
from games.numberGame import NumberState
from games.quizGame import QuizState
from secrets import token_hex
import json

app = Flask(__name__)
app.secret_key = token_hex(32)


def save_state(key, state):
    session[key] = json.dumps(state.serialize())


def load_state(key, cls):
    raw = session.get(key)
    if not raw:
        return None
    obj = json.loads(raw)
    return cls.deserialize(obj)

templates = {
    'layout': 'layout.html',
    'index': 'index_tpl.html',
    'naval': 'naval_tpl.html',
    'hangman': 'hangman_tpl.html',  
    'hanoi': 'hanoi_tpl.html',
    'jokenpo': 'jokenpo_tpl.html',
    'number': 'number_tpl.html',
    'quiz': 'quiz_tpl.html',
}


@app.route('/')
def index():
    return render_template(templates['index'])


@app.route('/naval')
def naval():
    if 'naval' not in session:
        save_state('naval', NavalGameState())
    return render_template(templates['naval'])

@app.route('/naval/state')
def naval_state():
    g = load_state('naval', NavalGameState)
    if not g:
        g = NavalGameState()
        save_state('naval', g)
    message = ''
    if g.all_sunk():
        message = 'Todos os navios destruídos!'
    return jsonify({'board': g.board, 'message': message})

@app.route('/naval/new')
def naval_new():
    g = NavalGameState()
    save_state('naval', g)
    return redirect(url_for('naval'))

@app.route('/naval/play', methods=['POST'])
def naval_play():
    data = request.get_json(silent=True) or {}
    try:
        y = int(data.get('y', data.get('row', 0)))
        x = int(data.get('x', data.get('col', 0)))
    except:
        return jsonify({'result': 'entrada inválida', 'board': None}), 400

    g = load_state('naval', NavalGameState)
    if not g:
        g = NavalGameState()
    res = g.play(y, x)
    save_state('naval', g)
    finished = g.all_sunk()
    return jsonify({**res, 'finished': finished, 'board': g.board})

@app.route('/hangman')
def hangman():
    if 'hangman' not in session:
        save_state('hangman', HangmanState())
    return render_template(templates['hangman'])

@app.route('/hangman/state')
def hangman_state():
    g = load_state('hangman', HangmanState)
    if not g:
        g = HangmanState()
        save_state('hangman', g)
    status = 'playing'
    if '_' not in g.ans:
        status = 'won'
    elif g.lifes <= 0:
        status = 'lost'
    return jsonify({'ans': ''.join(g.ans), 'lifes': g.lifes, 'status': status})

@app.route('/hangman/play', methods=['POST'])
def hangman_play():
    data = request.get_json(silent=True) or {}
    letter = (data.get('letter') or '').lower()
    if not letter or len(letter) != 1 or not letter.isalpha():
        return jsonify({'error': 'letra inválida'}), 400

    g = load_state('hangman', HangmanState)
    if not g:
        g = HangmanState()
    res = g.play_letter(letter)
    save_state('hangman', g)
    return jsonify(res)

@app.route('/hangman/new')
def hangman_new():
    g = HangmanState()
    save_state('hangman', g)
    return redirect(url_for('hangman'))

@app.route('/hanoi')
def hanoi():
    if 'hanoi' not in session:
        save_state('hanoi', HanoiState())
    return render_template(templates['hanoi'])

@app.route('/hanoi/state')
def hanoi_state():
    g = load_state('hanoi', HanoiState)
    if not g:
        g = HanoiState()
        save_state('hanoi', g)
    return jsonify({'tower': g.get_tower()})

@app.route('/hanoi/move', methods=['POST'])
def hanoi_move():
    data = request.get_json(silent=True) or {}
    try:
        init = int(data.get('init'))
        dest = int(data.get('dest'))
    except:
        return jsonify({'ok': False, 'error': 'entrada inválida'}), 400

    g = load_state('hanoi', HanoiState)
    if not g:
        g = HanoiState()
    res = g.move(init, dest)
    save_state('hanoi', g)
    return jsonify(res)

@app.route('/hanoi/new')
def hanoi_new():
    save_state('hanoi', HanoiState())
    return redirect(url_for('hanoi'))


@app.route('/jokenpo')
def jokenpo():
    if 'jokenpo' not in session:
        save_state('jokenpo', JokenpoState())
    return render_template(templates['jokenpo'])

@app.route('/jokenpo/play', methods=['POST'])
def jokenpo_play():
    data = request.get_json(silent=True) or {}
    try:
        p1 = int(data.get('p1', 1))
    except:
        return jsonify({'error': 'entrada inválida'}), 400
    g = load_state('jokenpo', JokenpoState)
    if not g:
        g = JokenpoState()
    res = g.play(p1)
    save_state('jokenpo', g)
    return jsonify(res)


@app.route('/number')
def number():
    if 'number' not in session:
        save_state('number', NumberState())
    return render_template(templates['number'])

@app.route('/number/play', methods=['POST'])
def number_play():
    data = request.get_json(silent=True) or {}
    try:
        n = int(data.get('n'))
    except:
        return jsonify({'error': 'entrada inválida'}), 400
    g = load_state('number', NumberState)
    if not g:
        g = NumberState()
    res = g.play(n)
    save_state('number', g)
    return jsonify(res)

@app.route('/quiz')
def quiz():
    if 'quiz' not in session:
        save_state('quiz', QuizState())
    return render_template(templates['quiz'])

@app.route('/quiz/ask')
def quiz_ask():
    g = load_state('quiz', QuizState)
    if not g:
        g = QuizState()
    q = g.ask()
    save_state('quiz', g)
    return jsonify({'question': q})

@app.route('/quiz/answer', methods=['POST'])
def quiz_answer():
    data = request.get_json(silent=True) or {}
    try:
        ans = int(data.get('ans'))
    except:
        return jsonify({'error': 'entrada inválida'}), 400
    g = load_state('quiz', QuizState)
    if not g:
        g = QuizState()
    res = g.answer(ans)
    save_state('quiz', g)
    return jsonify(res)

app.run(debug=True)
