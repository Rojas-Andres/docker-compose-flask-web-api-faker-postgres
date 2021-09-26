from sqlalchemy import Column,String , Integer
#from db import Base,engine
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from api import db

class Frutas(db.Model):
    __tablename__ = 'frutas'
    id = db.Column(db.Integer,autoincrement=True , primary_key=True)
    nombre_fruta = db.Column(db.String(70),unique=True)
