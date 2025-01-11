# Criar os formulários do site
from flask_wtf import FlaskForm
from flask import render_template, redirect, url_for, flash
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, InputRequired
from project.models import usuario
from project import db
from project import app

class FormCadastrar(FlaskForm):
    nome = StringField('Digite seu nome:', validators=[DataRequired(), Length(2, 50)])
    telefone = StringField('Telefone:', validators=[DataRequired(), Length(10, 15)])
    data_nascimento = DateField('Data de Nascimento:', format='%Y-%m-%d', validators=[DataRequired()])
    botao_confirmar = SubmitField('Cadastrar')

class FormLogin(FlaskForm):
    nome = StringField('Digite seu nome:', validators=[DataRequired(), Length(2, 50)])
    telefone = StringField('Telefone:', validators=[DataRequired(), Length(10, 15)])
    botao_entrar = SubmitField('Entrar')


class AgendamentoForm(FlaskForm):
    usuario_id = StringField('ID do Usuário', validators=[DataRequired()])
    tipo_cabelo = SelectField('Tipo de Corte', choices=[('degrade', 'Degrade'), ('social', 'Social'), 
                                                        ('mullet', 'Mullet'), ('navalhado', 'Navalhado'),
                                                        ('militar', 'Militar')], validators=[DataRequired()])
    horario_cabelo = SelectField('Horário', choices=[('7a12', '7h as 12h'), ('13a18', '13h as 20h')], 
                                 validators=[DataRequired()])
    forma_pagamento = SelectField('Forma de Pagamento', choices=[('pix', 'Pix'), ('dinheiro', 'Dinheiro'),
                                                                 ('cartao_credito', 'Cartão de Crédito'),
                                                                 ('cartao_debito', 'Cartão de Débito')],
                                 validators=[DataRequired()])
    data = DateField('Data de Agendamento', validators=[DataRequired()])
    submit = SubmitField('Agendar')
'''@app.route("/cadastrar", methods=['GET','POST'])
def cadastro():
    formCadastrar = FormCadastrar
    if formCadastrar.validate_on_submit():
        nome = formCadastrar.nome.data
        telefone = formCadastrar.telefone.data
        data = formCadastrar.data.data


        novo_usuario = usuario(nome=nome,telefone=telefone,data=data)
        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for("login.html"))
    return render_template("cadastrar.html", form=formCadastrar)

@app.route("/login", methods = ["GET","POST"])
def login():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        nome = formlogin.nome.data
        telefone = formlogin.telefone.data

        novo_usuario = usuario.query.filter_by(nome=nome, telefone=telefone).first()
        if novo_usuario:
            return redirect(url_for("index.html"))
        else: 
            flash("Credenciais invalidas. Tente novamente.", "error")

        return render_template("login.html", form=formlogin)            
        #tem q colocar as telas de login e cadastro para poder funcionar'''