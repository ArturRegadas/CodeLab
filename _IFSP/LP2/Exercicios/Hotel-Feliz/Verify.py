from functools import wraps
from flask import session, jsonify
from models.Usuario import Usuario

def perfil_required(allowed_perfis):
    if isinstance(allowed_perfis, str):
        allowed = {allowed_perfis}
    else:
        allowed = set(allowed_perfis)

    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_id = session.get("user_id")
            if not user_id:
                return jsonify({"error": "Autenticação requerida"}), 401
            user = Usuario.query.get(user_id)
            if not user or not user.perfil or user.perfil.nome_perfil not in allowed:
                return jsonify({"error": "Acesso negado"}), 403
            return f(*args, **kwargs)
        return wrapped
    return decorator