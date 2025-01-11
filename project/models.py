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

class Agendado(db.Model):
    __tablename__ = 'agendado'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    corte = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(100), nullable=False)
    dt = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.String(100), nullable=False)

    usuario = db.relationship('Usuario', backref='agendamentos')  # Relacionamento com o modelo Usuario

    # Adicionando o extend_existing
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return f'<Corte {self.corte}>'


