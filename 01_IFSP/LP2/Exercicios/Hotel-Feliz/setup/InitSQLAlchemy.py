from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from secrets import token_hex
db = SQLAlchemy()
def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enetemnemoqfalar_user:tzEmYHGIdvjlMyLYNwyasHwi026ukrvn@dpg-d4cgqmripnbc739f4s50-a.oregon-postgres.render.com/enetemnemoqfalar'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = token_hex(32)
    db.init_app(app)