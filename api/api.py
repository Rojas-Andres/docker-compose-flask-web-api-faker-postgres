from flask import Flask, flash,session,jsonify
from db import Session , engine,connection_db
from flask_sqlalchemy import SQLAlchemy
import requests
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
session = Session()
from models import *
@app.route('/')
def hola():
    return jsonify({"mensaje":'holas'})
@app.route('/crear_registros')
def crear_registros():
    print("entre ")
    url = 'http://faker-service/datos'
    response = requests.get(url)
    response_json = json.loads(response.text)
    '''
    for i in range(response_json["datos"]):
        #data = DataFaker(nombre=i["name"], nombre_compania=i["company_email"], ciudad=i["city"],direccion=i["address"],telefono=i["phone_number"])
        #db.session.add(data)
        #db.session.commit()
        print(i)
    '''
    for i in response_json["datos"]:
        data = DataFaker(nombre=i["name"], nombre_compania=i["company_email"], ciudad=i["city"],direccion=i["address"],telefono=i["phone_number"])
        db.session.add(data)
        db.session.commit()
    return response_json
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
