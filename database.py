from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template
from flask_login import UserMixin



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'

db = SQLAlchemy(app)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    
db.create_all()


if __name__ == "__main__":
    app.run(debug=True)