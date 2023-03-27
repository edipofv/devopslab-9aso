from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Código de Pipeline do Édipo"

if __name__ == '__main__':
    app.run()