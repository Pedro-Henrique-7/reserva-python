from flask import Flask, render_template, request, redirect, url_for
from database import listar_recursos, adicionar_recursos, reservar_recurso


app = Flask(__name__)

@app.route('/') #cria rota inicial 
def home():
    recursos = listar_recursos()
    return render_template('home.html', recursos=recursos)

@app.route ('/adicionar-recurso', methods=['GET', 'POST']) #mostra formulario para adicionar um get e processa con post
def adicionar_recurso_view():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        adicionar_recursos(nome, descricao)
        return redirect(url_for('home'))
    return render_template('adicionar_recurso.html')

@app.route ('/reservar', methods= ['GET', 'POST'])
def reservar_view():
    recursos = listar_recursos()

    if request.method == 'POST':
        recurso_id= request.form['recurso_id']
        usuario_nome = request.form['usuario_nome']
        data = request.form['data']
        reservar_recurso(recurso_id, usuario_nome, data)
        return redirect(url_for('home'))
    
    return render_template('reservar.html', recursos = recursos)

if __name__ == '__main__':
    app.run(debug=True)