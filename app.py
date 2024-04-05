from flask import Flask, request, jsonify
from models import Produto, Usuario, Setor, Categoria
app = Flask(__name__)

produtos = {}
usuarios = {}
setores = {}
categorias = {}

@app.route('/produtos', methods=['GET', 'POST'])
def handle_produtos():
    if request.method == 'POST':
        dados = request.get_json()
        produto = Produto(dados['id'], dados['nome'])
        produtos[produto.id] = {
            'id': int(produto.id),
            'nome': produto.nome
        }
        return jsonify(produtos.get(produto.id))
    else:
        id = request.args.get('id')
        if id:
            id = int(id)
            if id in produtos.keys():
                return jsonify(produtos.get(id))
            else:
                return 'Produto não encontrado'
        else:
            return jsonify(produtos)
        
@app.route('/usuarios', methods=['GET', 'POST'])
def handle_usuarios():
    if request.method == 'POST':
        dados = request.get_json()
        usuario = Usuario(dados['id'], dados['nome'])
        usuarios[usuario.id] = {
            'id': int(usuario.id),
            'nome': usuario.nome
        }
        return jsonify(usuarios.get(usuario.id))
    else:
        id = request.args.get('id')
        if id:
            id = int(id)
            if id in usuarios.keys():
                return jsonify(usuarios.get(id))
            else:
                return 'Usuário não encontrado'
        else:
            return jsonify(usuarios)
        
@app.route('/setores', methods=['GET', 'POST'])
def handle_setores():
    if request.method == 'POST':
        dados = request.get_json()
        setor = Setor(dados['id'], dados['nome'])
        setores[setor.id] = {
            'id': int(setor.id),
            'nome': setor.nome
        }
        return jsonify(setores.get(setor.id))
    else:
        id = request.args.get('id')
        if id:
            id = int(id)
            if id in setores.keys():
                return jsonify(setores.get(id))
            else:
                return 'Setor não encontrado'
        else:
            return jsonify(setores)
        
@app.route('/categorias', methods=['GET', 'POST'])
def handle_categorias():
    if request.method == 'POST':
        dados = request.get_json()
        categoria = Categoria(dados['id'], dados['nome'])
        categorias[categoria.id] = {
            'id': int(categoria.id),
            'nome': categoria.nome
        }
        return jsonify(categorias.get(categoria.id))
    else:
        id = request.args.get('id')
        if id:
            id = int(id)
            if id in categorias.keys():
                return jsonify(categorias.get(id))
            else:
                return 'Categoria não encontrado'
        else:
            return jsonify(categorias)
    
    
if __name__ == '__main__':
    app.run(debug=True)
