from flask import Flask, render_template, request, redirect, url_for
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hola():
    if request.method == 'POST':
        return render_template('index.html') 
    url = 'http://api-service/'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return render_template('index.html')

@app.route('/crear_registros', methods=['POST'])
def crear_registros():
    #Crear registros
    url = 'http://api-service/crear_registros'
    response = requests.get(url)
    return render_template('creados.html')


@app.route('/registros', methods=['GET'])
def registros(): 
    # Renderizar la cantidad de registros
    url = 'http://api-service/registros_faker'
    response = requests.get(url)
    response_json = json.loads(response.text)

    return render_template('registros.html',data=response_json["data"])

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
