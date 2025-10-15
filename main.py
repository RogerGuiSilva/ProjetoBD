from flask import Flask

app = Flask(__name__)

# Rota principal (raiz)
@app.route("/", methods=['GET'])
def home():
    return {
        'message': 'Bem-vindo à API!'
    }

# Rota da API
@app.route("/api", methods=['GET'])
def index():
    return {
        'message': 'API rodando'
    }

if __name__ == '__main__':
    app.run(debug=True)
