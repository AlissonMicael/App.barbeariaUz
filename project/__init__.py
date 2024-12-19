from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "comida"

# Configuração da URL de conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/uzcabas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importa os modelos e rotas aqui para evitar importações circulares
from project.route import home_route, login_route, cabelo_route, barba_route, combo_route, barbeiro_route, cadastrar_route

app.register_blueprint(home_route)
app.register_blueprint(login_route, url_prefix='/login')
app.register_blueprint(cabelo_route, url_prefix='/cabelo')
app.register_blueprint(barba_route, url_prefix='/barba')
app.register_blueprint(combo_route, url_prefix='/combo')
app.register_blueprint(barbeiro_route, url_prefix='/barbeiro')
app.register_blueprint(cadastrar_route, url_prefix='/oi')

# Cria as tabelas no banco de dados, se não existirem
with app.app_context():
    db.create_all()  # Crie as tabelas

