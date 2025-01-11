from project import db
db.metadata.clear()

print(db)

class usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    dt_nascimento = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.Nome}>'

class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String(100), nullable=False)  # Nome do cliente logado
    data = db.Column(db.String(10), nullable=False)
    tipo_cabelo = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    forma_pagamento = db.Column(db.String(50), nullable=False)
    profissional = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Agendamento {self.tipo_cabelo} - {self.data}>'


