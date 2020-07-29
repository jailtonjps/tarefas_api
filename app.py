from flask import Flask, jsonify,request
import json

app = Flask(__name__)

tarefas = [
    {
         'id': 0,
         'responsavel':'Jailton',
         'tarefa': 'Desenvolver metodo GET',
         'status': 'concluido'
    },
    {
         'id': 1,
         'responsavel':'Miguel',
         'tarefa': 'Desenvolver metodo POST',
         'status': 'pendente'

    }
]
# devolve uma tarefa pelo ID, tbem altera e deleta uma tarefa
@app.route('/tar/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro','mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})

# Lista todas as tarefas e permite incluir uma nova tarefa
@app.route('/tar/', methods=['POST','GET'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method =='GET':
        return jsonify(tarefas)


if __name__ == '__main__':
    app.run(debug=True)

