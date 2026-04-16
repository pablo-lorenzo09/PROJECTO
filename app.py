from flask import Flask, render_template, request, redirect, session, flash
import mysql
import mysql.connector
from model.hamburguer import recuperar_hamburguers
from model.hamburguer import recuperar_hamburguers_destaques
from model.hamburguer import recuperar_produto
from model.hamburguer import cadastrar

app = Flask (__name__)

@app.route("/")
@app.route("/home",methods=["GET"])
def pag_principal():
    hamburguers = recuperar_hamburguers()
    hamburguers_destaque = recuperar_hamburguers_destaques()
    return render_template("index.html", hamburguers = hamburguers, hamburguers_destaque = hamburguers_destaque)


@app.route("/pagina2/<int:id>")
def pag_dois(id):
    lanche = recuperar_produto(id)
    return render_template("produto.html", lanche = lanche)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)



@app.route("/cadastro")
def tela_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro",methods=["POST"])
def tela_cadastro_post():
    nome = request.form.get("usuario")
    senha = request.form.get("senha")
    cadastrar(nome, senha)
    return render_template("cadastro.html")