
from flask import Flask, request, redirect, url_for, render_template
from models.usuario_model import Usuario
from models.conexao import session
app = Flask(__name__)

from models.usuario_model import *
from models.cliente_model import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user')
def user():
    usuarios = session.query(Usuario).all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/user/create', methods=['POST'])
def create_user():
    nome = request.form['nome']
    login = request.form['login']
    senha = request.form['senha']
    email = request.form['email']
    telefone = request.form['telefone']

    novo_usuario = Usuario(
        nome=nome,
        login=login,
        senha=senha,
        email=email,
        telefone=telefone
    )

    session.add(novo_usuario)
    session.commit()

    return redirect(url_for('user'))

@app.route('/gerenciarequipamentos')
def gerenciarequipamentos():
    return render_template('gerenciar_equipamentos.html')

@app.route('/cadastrarequipamento')
def cadastrarequipamento():
    return render_template('cadastrar_equipamento.html')

@app.route('/listaequipamento')
def listaequipamento():
    return render_template('lista_equipamento.html')

@app.route('/consultaequipamento')
def consultaequipamento():
    return render_template('consulta_equip.html')

@app.route('/atualizaequipamento')
def atualizaequipamento():
    return render_template('atualizar.html')

@app.route('/telaprincipal', methods=['Post'])
def telaPrincipal():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if(usuario == "123"  and senha == "ab"):
        return render_template("tela_principal.html")
    else:
        return  render_template('login.html')
    
if __name__ == "__main__":
    app.run(debug=True)