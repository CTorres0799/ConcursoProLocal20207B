from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import Column,Integer,String, ForeignKey
from flask_login import UserMixin
#from app import db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()



#PedriñoGames
class Usuario(UserMixin, db.Model):
    __tablename__='Usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String, nullable= False)
    sexo = Column(String, nullable = False)
    telefono = Column(String, nullable = False)
    email = Column(String, nullable = False)
    estatus = Column(String, nullable = False)
    tipo = Column(String, nullable = False)
    password_hash= Column(String(16), nullable = False)

    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def validarPassword(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True
    def is_active(self):
        if self.estatus == 'A':
            return True
        else:
            return False
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.idUsuario
    def is_admin(self):
        if self.tipo =='A':
            return True
        else:
            return False
    def getTipo(self):
        return self.tipo
    def validar(self, email, password):
        user = Usuario.query.filter_by(email='email', estatus='A').first()
        if user!= None:
            if user.validarPassword(password):
                return user
        else:
            return None

#CRISTIAN DEVELOPED
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
        noControl = self.consultaIndividual()
        db.session.delete(noControl)
        db.session.commit()
    def consultaIndividual(self):
       Alumnos = self.query.get(self.noControl)
       return Alumnos
#FIN ALUMNOS

#INICIO CATEGORIAS
class Categorias(db.Model):
    __tablename__='Categorias'
    idCategoria = Column(Integer,primary_key=True)
    nombre = Column((String(30)))
    semestreLimite = Column((String(2)))
    idProPue = Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        Categorias = self.query.all()
        return Categorias
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        categoria = self.consultaIndividual()
        db.session.delete(categoria)
        db.session.commit()
    def consultaIndividual(self):
        categoria = self.query.get(self.idCategoria)
        return categoria
#FIN CATEGORIAS

#INICIO DOCENTES
class Docentes (db.Model):
    __tablename__='Docentes'
    idDocente = Column(Integer,primary_key=True)
    escolaridad = Column(String(50))
    especialidad = Column(String(50))
    cedula = Column(Integer)
    idCarrera = Column(Integer)
    idUsuario = Column(Integer)
    noControl = Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        Docentes = self.query.all()
        return Docentes
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        Docentes = self.consultaIndividual()
        db.session.delete(Docentes)
        db.session.commit()
    def consultaIndividual(self):
        Docentes = self.query.get(self.idDocente)
        return Docentes
#FIN DOCENTES

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

    def insert(self):
        db.session.add(self)
        db.session.add()
    def consultarGeneral(self):
        docentes = self.query.all()
        return docentes


