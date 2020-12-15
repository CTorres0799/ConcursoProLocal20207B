<<<<<<< HEAD
=======
from symbol import return_stmt
from urllib import request

from Tools.scripts.make_ctype import method
>>>>>>> 6384bad8b5d9a4ee3784df95c1510e7636f444cd
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Categoria


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://concursoprog_user:hola.123@localhost/ConcursoPro20207B'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#db = SQLAlchemy(app)

mysql = MYSQL(app)
app.secret_key = '123'

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/add contact', method=['POST'])
def add_contact():
    if request.method == 'POST':
        Usuario = request.form['Usuario']
        password = request.form['password']
     

@app.route('/login', methods =['GET','POST'])
def login():
    login_form = forms.LoginForm()
    if request.method == 'POST' and login_form.validate():
        pass
    return render_template('Index.html', form = login_form)

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