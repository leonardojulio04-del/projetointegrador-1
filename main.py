from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

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
        return render_template("consulta_equip.html")
    else:
        return  render_template('login.html')

app.run(debug=True)