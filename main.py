#biblioteca Flask sendo importada
from project import app

#executa o servidor 
if __name__ == "__main__":
    app.run(debug=True)