from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect
from models.cliente import Cadastrocliente
from conection.conexao import *


db.create_all()
db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro_clientes")
def cadastro_clientes():
    return render_template("cadastro_clientes.html")


@app.route("/editar_clientes/<int:id>")
def editar_clientes(id):
    cliente = Cadastrocliente.query.filter(Cadastrocliente.id == id).first()
    return render_template("editar_clientes.html", cliente=cliente)


@app.route("/listar_clientes")
def listar_clientes():
    clientes = Cadastrocliente.query.all()
    return render_template("listar_clientes.html", clientes=clientes)


@app.route("/cadastro", methods=["POST"])
def cadastro():
    if request.method == "POST":
        if (
            request.form["nome"]
            and request.form["razao_social"]
            and request.form["cnpj_cpf"]
            and request.form["cidade"]
            and request.form["UF"]
            and request.form["email"]
            and request.form["telefone"]
        ):
            cliente = Cadastrocliente(
                request.form["nome"],
                request.form["razao_social"],
                request.form["cnpj_cpf"],
                request.form["cidade"],
                request.form["UF"],
                request.form["email"],
                request.form["telefone"],
            )
            db.session.add(cliente)
            db.session.commit()
            return render_template(
                "cadastro_clientes.html", mensagem="Cadastro efetuado com sucesso!"
            )
        else:
            return render_template(
                "cadastro_clientes.html", mensagem="Erro no cadastro!"
            )


@app.route("/atualizar", methods=["POST"])
def atualizar():
    if request.method == "POST":
        if (
            request.form["id"]
            and request.form["nome"]
            and request.form["razao_social"]
            and request.form["cnpj_cpf"]
            and request.form["cidade"]
            and request.form["UF"]
            and request.form["email"]
            and request.form["telefone"]
        ):
            cliente = Cadastrocliente.query.filter(
                Cadastrocliente.id == request.form["id"]
            ).first()
            cliente.nome = request.form["nome"]
            cliente.razao_social = request.form["razao_social"]
            cliente.cnpj_cpf = request.form["cnpj_cpf"]
            cliente.cidade = request.form["cidade"]
            cliente.UF = request.form["UF"]
            cliente.email = request.form["email"]
            cliente.telefone = request.form["telefone"]
            db.session.add(cliente)
            db.session.commit()
            flash("Atualizado com sucesso!")
            return redirect(url_for("listar_clientes"))
        else:
            return render_template(
                "listar_clientes.html", mensagem="Erro na atualização!"
            )


if __name__ == "__main__":
    app.run(debug=True)
