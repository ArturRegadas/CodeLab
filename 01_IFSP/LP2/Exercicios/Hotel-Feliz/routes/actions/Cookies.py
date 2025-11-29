from flask import Blueprint, make_response, jsonify, request

cookies_bp = Blueprint("cookies", __name__)

@cookies_bp.route("/set_theme", methods=["POST"])
def set_theme():
    data = request.json or {}
    theme = data.get("theme", "light")
    resp = make_response(jsonify({"message": "Tema salvo", "theme": theme}))
    
    resp.set_cookie("theme_bg", theme, max_age=30*24*3600, httponly=False)
    return resp


@cookies_bp.route("/get_theme", methods=["GET"])
def get_theme():
    theme = request.cookies.get("theme_bg", "light")
    return jsonify({"theme": theme})