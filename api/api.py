from flask import Flask, flash,session,jsonify
from db import Session , engine,connection_db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
session = Session()
from models import *
@app.route('/')
def hola():
    return jsonify({"mensaje":'holas'})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
