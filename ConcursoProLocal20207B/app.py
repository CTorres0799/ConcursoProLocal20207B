from symbol import return_stmt
from urllib import request

from Tools.scripts.make_ctype import method
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Categoria

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://concursoprog_user:hola.123@localhost/ConcursoPro20207B'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#db = SQLAlchemy(app)

@app.route('/')
def Index():
    return  'Hello World'

@app.route('/add_alumno')
def add_alumno():
    return 'Añadir Contacto'

@app.route('/editar')
def editar_alumno():
    return 'Editando Alumno'

@app.route('/eliminar')
def eliminar_alumno():
    return 'Alumno Eliminado'

#Inicio CRUD tabla Categorias

@app.route('/categorias/new')
def nuevaCategoria():
    return render_template('Categorias/nuevaCategoria.html')
@app.route('/Categorias/save',methods=['POST'])
def guardarCategoria():
    categoria = Categoria()
    #categoria.idCategoria = request.form['idCategoria']
    #categoria.insertar()
    categoria.nombre = request.form['nombre']
    #categoria.insertar()
    categoria.semestreLimite = request.form['semestreLimite']
    #categoria.insertar()
    #categoria.idProPue = request.form['idProPue']
    categoria.insertar()
    return 'Categoria Registrada con Exito'
#FIN CRUD CATEGORIAS

if __name__ == '__main__':
 db.init_app(app)
 app.run(port = 3000, debug=True)