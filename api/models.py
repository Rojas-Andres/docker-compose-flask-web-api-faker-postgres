from sqlalchemy import Column,String , Integer
#from db import Base,engine
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from api import db

class DataFaker(db.Model):
    __tablename__ = 'datafaker'
    id = db.Column(db.Integer,autoincrement=True , primary_key=True)
    nombre = db.Column(db.String(255),unique=True)
    nombre_compania = db.Column(db.String(100),unique=True)
    ciudad = db.Column(db.String(120),unique=True)
    direccion = db.Column(db.String(200),unique=True)
    telefono = db.Column(db.String(40),unique=True)
