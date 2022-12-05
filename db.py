from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mibasedatos.sqlite', echo=True)
base = declarative_base()

class Usuario (base):
    __tablename__ = 'Usuario'
    usuario_id = Column(Integer, primary_key=True)
    nombre = Column(String)
    contrasena = Column(String)

    def __init__(self, usuario_id, nombre, contrasena):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.contrasena = contrasena

class Lenguaje (base):
    __tablename__ = 'Lenguaje'
    lenguaje_id = Column(Integer, primary_key=True)
    nombre = Column(String)
    propietario = Column(String)

    def __init__(self, lenguaje_id, nombre, propietario):
        self.lenguaje_id = lenguaje_id
        self.nombre = nombre
        self.propietario = propietario

class Proyecto (base):
    __tablename__ = 'Proyecto'
    proyecto_id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

    def __init__(self, proyecto_id , nombre, descripcion):
        self.proyecto_id = proyecto_id
        self.nombre = nombre
        self.descripcion = descripcion
        
base.metadata.create_all(engine)