from flask import Flask, render_template, request, redirect, session, flash
import mysql
import mysql.connector
from model.hamburguer import recuperar_hamburguers
from model.hamburguer import recuperar_hamburguers_destaques

app = Flask (__name__)

@app.route("/")
@app.route("/home",methods=["GET"])
def pag_principal():
    hamburguers = recuperar_hamburguers()
    hamburguers_destaque = recuperar_hamburguers_destaques()
    return render_template("index.html", hamburguers = hamburguers, hamburguers_destaque = hamburguers_destaque)

@app.route("/pagina2")
def pag_dois():
    return render_template("pagina2.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)