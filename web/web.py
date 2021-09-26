from flask import Flask, render_template, request, redirect, url_for,jsonify
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Renderizar la cantidad de registros
    url = 'http://api-service/registros_faker'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return render_template('index.html',data=response_json["data"])

@app.route('/registros', methods=['GET'])
def registros(): 
    # Renderizar la cantidad de registros
    url = 'http://api-service/registros_faker'
    response = requests.get(url)
    response_json = json.loads(response.text)

    return jsonify({"data":response_json["data"]})

@app.route('/eliminar_registros', methods=['POST'])
def eliminar_registros(): 
    # Renderizar la cantidad de registros
    url = 'http://api-service/eliminar_registros'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return redirect(url_for('index'))

@app.route('/crear_registros', methods=['POST'])
def crear_registros():
    #Crear registros
    url = 'http://api-service/crear_registros'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
