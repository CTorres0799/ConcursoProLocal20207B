from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename___ = 'users'

    id = ()



    def __int__(self, nombre, password):
        self.nombre = nombre
        sefl.password = self.__create__password(password)

    #def  create