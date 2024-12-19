#-----#
#Home
#-----#
from flask_wtf import FlaskForm
from flask import render_template, redirect, url_for, flash
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, InputRequired

from project import db
from project.models import usuario

from flask import Blueprint, render_template
from project.models import db

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

#-----#
#Login
#-----#

from flask import Blueprint, render_template

login_route = Blueprint('login', __name__)

@login_route.route('/')
def login():
    return render_template('login.html')

"""
Rota de Clientes

    - /login/ (GET) - listar clientes
    - /login/novo (GET) - renderiza um formulario para criar um novo cliente
    - /login/<id>/delete (DELETE) - deletar o registro

"""
# @login_route.route('/')
# def listar_clientes():
#     return render_template('lista_clientes_templat.html')

# @login_route.route('/novo')
# def inserir_clientes():
#     return render_template('form_cliente.html')

# @login_route.route('/<int:cliente_id>/delete', methods=['PUT'])
# def deletar_cliente(cliente_id):
#     return {'pagina':"Deletar_de_clientes"} 

#-----#
#cadastro
#-----#

from flask import Blueprint, render_template

cadastrar_route = Blueprint('cadastrar', __name__)

@cadastrar_route.route('/')
def cadastrar():
    return render_template('cadastrar.html')

#-----#
#Cabelo
#-----#

from flask import Blueprint, render_template

cabelo_route = Blueprint('cabelo', __name__)

@cabelo_route.route('/')
def mostra_cabelos():
    return render_template('cabelo.html')

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

