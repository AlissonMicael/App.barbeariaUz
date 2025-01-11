#-----#
#Home
#-----#
from flask_wtf import FlaskForm
from flask import render_template, redirect, url_for, flash, request, session
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, InputRequired

from . import db
from .models import usuario, Agendamento

from flask import Blueprint, render_template
from project.models import db

from .forms import FormCadastrar, FormLogin, AgendamentoForm


home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

#-----#
#Login
#-----#

from flask import Blueprint, render_template

login_route = Blueprint('login', __name__)

@login_route.route('/', methods=['GET', 'POST'])
def login():    
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        nome = formLogin.nome.data
        telefone = formLogin.telefone.data

        # Verificar credenciais
        usuario_existente = usuario.query.filter_by(nome=nome, telefone=telefone).first()
        if usuario_existente:
            session["usuario"] = nome
            flash("Login realizado com sucesso!", "success")
            return redirect('/')  # Redireciona para uma página principal
        else:
            flash("Credenciais inválidas. Tente novamente.", "error")    
    return render_template("login.html", form=formLogin)
#-----#
#cadastro
#-----#

from flask import Blueprint, render_template

cadastrar_route = Blueprint('cadastrar', __name__)

@cadastrar_route.route('/', methods=['GET', 'POST'])
def cadastrar():
    formCadastrar = FormCadastrar()
    if formCadastrar.validate_on_submit():
        nome = formCadastrar.nome.data
        telefone = formCadastrar.telefone.data
        data_nascimento = formCadastrar.data_nascimento.data.strftime('%Y-%m-%d')

        # Verificar se o usuário já existe
        if usuario.query.filter_by(nome=nome, telefone=telefone).first():
            flash("Usuário já cadastrado.", "error")
        else:
            # Criar novo usuário
            novo_usuario = usuario(nome=nome, telefone=telefone, dt_nascimento=data_nascimento, senha=telefone)
            db.session.add(novo_usuario)
            db.session.commit()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for("login.login"))

    return render_template("cadastrar.html", form=formCadastrar)


#-----#
#Cabelo
#-----#

from flask import Blueprint, render_template

cabelo_route = Blueprint('cabelo', __name__)

# Rota de agendamento
@cabelo_route.route('/', methods=['GET', 'POST'])
def agendar_cabelo():
    if "usuario" not in session:
        flash("Por favor, faça login para agendar.", "warning")
        return redirect('/')  # Redireciona para a página de login

    if request.method == "POST":
        # Obter dados do formulário
        nome_cliente = session["usuario"]  # Nome do cliente logado
        data = request.form.get("data")
        tipo_cabelo = request.form.get("tipo_cabelo")
        horario = request.form.get("horario_cabelo")
        forma_pagamento = request.form.get("forma_pagamento")
        profissional = request.form.get("profissional")

        # Criar uma nova entrada no banco de dados
        novo_agendamento = Agendamento(
            nome_cliente=nome_cliente,
            data=data,
            tipo_cabelo=tipo_cabelo,
            horario=horario,
            forma_pagamento=forma_pagamento,
            profissional=profissional
        )
        db.session.add(novo_agendamento)
        db.session.commit()

        flash("Agendamento realizado com sucesso!", "success")
        return redirect('/')
    
    return render_template("cabelo.html")





#-----#
#Barba
#-----#

from flask import Blueprint, render_template

barba_route = Blueprint('barba', __name__)

@barba_route.route('/')
def agendar_barba():
    if "usuario" not in session:
        flash("Por favor, faça login para agendar.", "warning")
        return redirect('/')  # Redireciona para a página de login

    if request.method == "POST":
        # Obter dados do formulário
        nome_cliente = session["usuario"]  # Nome do cliente logado
        data = request.form.get("data")
        tipo_cabelo = request.form.get("tipo_cabelo")
        horario = request.form.get("horario_cabelo")
        forma_pagamento = request.form.get("forma_pagamento")
        profissional = request.form.get("profissional")

        # Criar uma nova entrada no banco de dados
        novo_agendamento = Agendamento(
            nome_cliente=nome_cliente,
            data=data,
            tipo_cabelo=tipo_cabelo,
            horario=horario,
            forma_pagamento=forma_pagamento,
            profissional=profissional
        )
        db.session.add(novo_agendamento)
        db.session.commit()

        flash("Agendamento realizado com sucesso!", "success")
        return redirect('/')
    
    return render_template("barba.html")

#-----#
#Combo
#-----#

from flask import Blueprint, render_template

combo_route = Blueprint('combo', __name__)

@combo_route.route('/')
def agendar_combo():
    if "usuario" not in session:
        flash("Por favor, faça login para agendar.", "warning")
        return redirect('/')  # Redireciona para a página de login

    if request.method == "POST":
        # Obter dados do formulário
        nome_cliente = session["usuario"]  # Nome do cliente logado
        data = request.form.get("data")
        tipo_cabelo = request.form.get("tipo_cabelo")
        horario = request.form.get("horario_cabelo")
        forma_pagamento = request.form.get("forma_pagamento")
        profissional = request.form.get("profissional")

        # Criar uma nova entrada no banco de dados
        novo_agendamento = Agendamento(
            nome_cliente=nome_cliente,
            data=data,
            tipo_cabelo=tipo_cabelo,
            horario=horario,
            forma_pagamento=forma_pagamento,
            profissional=profissional
        )
        db.session.add(novo_agendamento)
        db.session.commit()

        flash("Agendamento realizado com sucesso!", "success")
        return redirect('/')
    
    return render_template("combo.html")
#-----#
#tela barb
#-----#

from flask import Blueprint, render_template

barbeiro_route = Blueprint('barbeiro', __name__)

@barbeiro_route.route('/')
def mostra_barbeiro():
    return render_template('tela_barbeiro.html')

@cabelo_route.route('/agendamentos/', methods=['GET'])
def exibir_agendamentos():
    if "usuario" not in session:
        flash("Por favor, faça login para visualizar seus agendamentos.", "warning")
        return redirect('/')  # Redireciona para a página de login

    # Obter os agendamentos do usuário logado
    nome_cliente = session["usuario"]
    agendamentos = Agendamento.query.filter_by(nome_cliente=nome_cliente).all()

    return render_template("agendamentos.html", agendamentos=agendamentos)
