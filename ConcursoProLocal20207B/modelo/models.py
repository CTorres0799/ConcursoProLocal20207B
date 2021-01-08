from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import Column,Integer,String, ForeignKey
from flask_login import UserMixin
#from app import db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

#KITIAN
class Categoria  (db.Model):
    __tablename__='Categorias'
    idCategoria = Column(Integer,primary_key=True)
    nombre = Column(String,unique=True)
    semestreLimite = Column(Integer)
    idProPue = Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        categorias = self.query.all()
        return  categorias
    def consultaIndividual(self):
        categorias = self.query.all()
        return  categorias

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

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        categorias = self.query.all()
        return categorias
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usuario = self.consultaInduvidual()
        db.session.delete(usuario)
        db.session.commit()
    def consultaIndividual(self):
        usuario = self.query.get(self.idUsuario)
        return usuario

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










    
