from app import app
from flask import render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from db import db
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/send", methods=["POST"])
def send():
    name  = request.form["name"]
    hp = request.form["hp"]
    poke_id = request.form["poke_id"]
    sql = text("INSERT INTO pokemon (name, hp, poke_id) VALUES (:name, :hp, :poke_id)")
    db.session.execute(sql, {"name":name, "hp":hp,"poke_id":poke_id})
    db.session.commit()
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/create_user")
def create_user():
    return render_template("create_user.html")

@app.route("/add_user")
def add_user():
    user = request.form["user"]
    password = request.form["password"]
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":user, "password":password})
    db.session.commit()
    return redirect()
