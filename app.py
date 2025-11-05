#1. instalamos a biblioteca flask no terminal com o comando: pip install flask
#2. importamos a biblioteca flask para nosso arquivo
from flask import Flask, make_response, jsonify, request
from bd_livros import livros
#bibliotecas
# jsonify = lista, dicionario em arquivos json
#  make_response = cria um objeto de resta HTTP completo, ele nao apenas retorna os dados, mas também permite personalizar
# cabeçalhos e status code. essa biblioteca vai transformar o JSON em resposta HTTP
#o jsonify funciona sem o make_response, usamos ele apenas para mais controle sobre A RESPOSTA, ou seja, para obter outros
#status for o 200
# 3. instanciamos o Flask ( criar um objeto a partir de uma classe)
# Uma instancia é o objeto real construido a partir desse molde
app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False


@app.route('/livros', methods=['GET'])
def get_livros():
    return make_response(jsonify(
        mensagem = 'Lista De Livros',
        dados = livros
    ))
# GET - Buscar por ID
@app.route('/livros/<int:id>' , methods=['GET'])
def get_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            return make_response(jsonify(                  
                mensagem = 'Livro encontrado', dados= livro 
            ))
    return make_response(jsonify(mensagem = 'Livro nao encontrado'),404)
# POST - Criar um novo livro
@app.route('/livros', methods=['POST'])
def create_livro():
    livro = request.json
    livros.append(livro)
    return make_response(jsonify(mensagem='Novo Livro adicionado com sucesso', dados=livro), 201)

# PUT - Atualizar livro ( substitui todos os dados)
@app.route('/livros/<int:id>', methods=['PUT'])
def update_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            novo_livro = request.json
            livro.update(novo_livro)
            return make_response(jsonify(mensagem=f'Livro id {id} atualizado com sucesso (PUT)',
                                         dados=livro))
    return make_response(jsonify(mensagem='Livro não encontrado'), 404)
# PATCH - Atualizar parcialmente um livro
@app.route('/livros/<int:id>', methods=['PATCH'])
def patch_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            dados = request.json
            livro.update(dados)
            return make_response(jsonify(mensagem='Livro não encontrado'),404)
# DELETE - Remover um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            livros.remove(livro)
            return make_response(jsonify(
                mensagem=f'Livro ID {id} removido com sucesso.',
                dados=livro
            ), 200)
    return make_response(jsonify(
        mensagem='Livro não encontrado'),)



if __name__ == '__main__':
    app.run(debug=True)