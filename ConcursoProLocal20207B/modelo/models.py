from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import Column,Integer,String
#from app import db
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