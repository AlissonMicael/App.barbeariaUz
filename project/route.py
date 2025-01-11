#-----#
#Home
#-----#
from flask_wtf import FlaskForm
from flask import render_template, redirect, url_for, flash
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, InputRequired

from . import db
from .models import usuario

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

@cabelo_route.route('/', methods=['GET', 'POST'])
class Agendado(db.Model):
    __tablename__ = 'agendado'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    corte = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(100), nullable=False)
    dt = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.String(100), nullable=False)

    usuario = db.relationship('Usuario', backref='agendamentos')  # Relacionamento com o modelo Usuario

    def __repr__(self):
        return f'<Corte {self.corte}>'

# Rota de agendamento
@cabelo_route.route('/', methods=['GET', 'POST'])
def agendamento():
    form = AgendamentoForm()  # Instancia o formulário
    if form.validate_on_submit():  # Verifica se o formulário foi submetido e é válido
        # Coletando dados do formulário
        data = form.data.data
        corte = form.tipo_cabelo.data
        horario = form.horario_cabelo.data
        preco = form.forma_pagamento.data
        usuario_id = form.usuario_id.data  # Supondo que o usuário esteja autenticado e tenha um ID
        
        # Criando um novo agendamento no banco de dados
        novo_agendamento = Agendado(
            id_usuario=usuario_id,
            corte=corte,
            horario=horario,
            dt=data,
            preco=preco
        )

        # Salvando no banco de dados
        db.session.add(novo_agendamento)
        db.session.commit()

        # Mensagem de sucesso
        flash('Agendamento realizado com sucesso!', 'success')
        return redirect(url_for('sucesso'))

#-----#
#Barba
#-----#

from flask import Blueprint, render_template

barba_route = Blueprint('barba', __name__)

@barba_route.route('/')
def mostra_barba():
    return render_template('barba.html')

#-----#
#Combo
#-----#

from flask import Blueprint, render_template

combo_route = Blueprint('combo', __name__)

@combo_route.route('/')
def mostra_combo():
    return render_template('combo.html')

#-----#
#tela barb
#-----#

from flask import Blueprint, render_template

barbeiro_route = Blueprint('barbeiro', __name__)

@barbeiro_route.route('/')
def mostra_barbeiro():
    return render_template('tela_barbeiro.html')

