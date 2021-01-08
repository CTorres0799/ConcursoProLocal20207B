from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import Column,Integer,String
#from app import db
db = SQLAlchemy()

#KITIAN
class Categorias(db.Model):
    __tablename__='Categorias'
    id = Column(Integer,primary_key=True)
    Nombre = Column(String(30),unique=True)
    SemestreLimite = Column(Integer)
    IdProPue = Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        categorias = self.query.all()
        return  categorias

#INICIO ALUMNOS
class Alumnos(db.Model):
    __tablename__='Alumnos'
    noControl = Column(Integer,primary_key=True)
    semestre = Column(String(2))
    idUsuario = Column(Integer)
    idCarrera = Column(Integer)
    idProRes = Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        Alumnos = self.query.all()
        return  Alumnos
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        Alumnos = self.consultaIndividual()
        db.session.delete(Alumnos)
        db.session.commit()
    def consultaIndividual(self):
       Alumnos = self.query.get(self.noControl)
       return Alumnos
#FIN ALUMNOS

class PPropuestos (db.Model):
    __tablename__='ProblemasPropuestos'
    idProPue = Column(Integer,primary_key=True)
    globo = Column(String(15))
    idProblema = Column(Integer)
    idEdicion = Column(Integer)
    idCategoria = Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        PP = self.query.all()
        return PP
class Docentes (db.Model):
    __tablename__='Docentes'
    idDocente = Column(Integer,primary_key=True)
    escolaridad = Column(String(50))
    especialidad = Column(String(50))
    cedula = Column(Integer)
    idCarrera = Column(Integer)
    idUsuario = Column(Integer)
    noControl = Column(Integer)
    def insert(self):
        db.session.add(self)
        db.session.add()
    def consultarGeneral(self):
        docentes = self.query.all()
        return docentes

