from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import Column,Integer,String,ForeignKey
from flask_login import UserMixin
#from app import db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()



#PedriñoGames
class Usuario(UserMixin,db.Model):
    __tablename__='Usuarios'

    idUsuario=Column(Integer,primary_key=True)
    nombre=Column(String,nullable= False)
    sexo=Column(String,nullable = False)
    telefono=Column(String,nullable = False)
    email=Column(String,nullable = False)
    estatus=Column(String,nullable = False)
    tipo=Column(String,nullable = False)
    password_hash=Column(String(128),nullable = False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        categorias=self.query.all()
        return categorias
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usuario=self.consultaIndividual()
        db.session.delete(usuario)
        db.session.commit()
    def consultaIndividual(self):
        usuario=self.query.get(self.idUsuario)
        return usuario
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    def validarPassword(self,password):
        return check_password_hash(self.password_hash,password)

    def is_authenticated(self):
        return True
    def is_active(self):
        if self.estatus=='A':
            return True
        else:
            return False
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.idUsuario
    def is_admin(self):
        if self.tipo=='Ad':
            return True
        else:
            return False
    def getTipo(self):
        return self.tipo
    def validar(self, email, password):
        user = Usuario.query.filter_by(email=email, estatus='A').first()
        if user != None:
            if user.validarPassword(password):
                return user
        else:
            return None
#FIN Usuarios

#inicio Carrera
class Carreras(db.Model):
    __tablename__='Carreras'
    idCarrera = Column(Integer,primary_key=True)
    noControl = Column(Integer)
    nombre = Column(String(50))
    siglas = Column(String(6))

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        Carreras = self.query.all()
        return Carreras
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        carrera = self.consultaIndividual()
        db.session.delete(carrera)
        db.session.commit()
    def consultaIndividual(self):
        carrera = self.query.get(self.idCarrera)
        return carrera
#fin de crud carrera

#inicio Equipos
class Equipos(db.Model):
    __tablename__='Equipos'
    idEquipo = Column(Integer,primary_key=True)
    idProRes = Column(Integer)
    idProPue = Column(Integer)
    nombre = Column(String(40))
    noControl1 =  Column(Integer)
    noControl2 = Column(Integer)
    noControl3 = Column(Integer)
    idDocentes = Column(Integer)
    idCategorias = Column(Integer)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        Equipos = self.query.all()
        return Equipos
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        equipos = self.consultaIndividual()
        db.session.delete(equipos)
        db.session.commit()
    def consultaIndividual(self):
        equipos = self.query.get(self.idEquipo)
        return equipos

#fin de crud  Equipos

#inicio Ediciones
class Ediciones(db.Model):
    __tablename__='Ediciones'
    idEdiciones = Column(Integer, primary_key=True)
    idProPue = Column(Integer)
    idProRes = Column(Integer)
    nombre = Column(String(40))
    fechaRegistro = Column(Integer)
    fechaEvento = Column(Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        Ediciones = self.query.all()
        return Ediciones
    def actualizar(self):
        db.session.merge()
        db.session.commit()
    def eliminar(self):
        ediciones = self.consultaIndividual()
        db.session.delete(ediciones)
        db.session.commit()
    def consultaIndividual(self):
        ediciones = self.query.get(self.idEdiciones)
        return ediciones
#fin  ediciones

#inicio ProblemasResueltos
class problemasResueltos(db.Model):
    __tablename__ = 'problemasResueltos'
    idProRes = Column(Integer, primary_key=True)
    idProPue = Column(Integer)
    idEquipo = Column(Integer)
    tiempo = Column(Integer)
    tiempoEjecicion = Column(Integer)
    puntaje = Column(Integer)

    def inserta(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        db.session.delete(self.consultaIndividual())
        db.session.commit()
    def consultaIndividual(self):
        return self.query.get(self.idProRes)
##fin de crud ProblemasResueltos
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


        categorias = self.query.all()
        return categorias

        Alumnos = self.query.all()
        return  Alumnos


    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):

        noControl = self.consultaIndividual()
        db.session.delete(noControl)


        #usuario = self.consultaInduvidual()
        #db.session.delete(usuario)
        db.session.commit()
    def consultaIndividual(self):
        usuario = self.query.get(self.idUsuario)
        return usuario
        Alumnos = self.consultaIndividual()
        db.session.delete(Alumnos)

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

#INICIO P.PROPUESTOS
class ProblemasPropuestos(db.Model):
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
        ProblemasPropuestos = self.query.all()
        return ProblemasPropuestos
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        ProblemasPropuestos = self.consultaIndividual()
        db.session.delete(ProblemasPropuestos)
        db.session.commit()
    def consultaIndividual(self):
        ProblemasPropuestos = self.query.get(self.idProPue)
        return ProblemasPropuestos
#FIN P.PROPUESTOS

#INICIO BANCO PROBLEMAS
class BancoProblemas(db.Model):
    __tablename__= 'bancoProblemas'
    idProblema = Column(Integer,primary_key=True)
    nombre = Column(String(50))
    puntos = Column(Integer)
    tiempoMaximo = Column(Integer)
    descripcion = Column(String(120))
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        BancoProblemas = self.query.all()
        return BancoProblemas
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        BancoProblemas = self.consultaIndividual()
        db.session.delete(BancoProblemas)
        db.session.commit()
    def consultaIndividual(self):
        BancoProblemas = self.query.get(self.idProblema)
        return BancoProblemas
#FIN BANCO PROBLEMAS

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



