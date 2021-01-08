#from urllib import request
#from Tools.scripts.make_ctype import method
from flask import Flask, render_template, request, abort, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Categoria, Usuario
import json

app = Flask(__name__)
app.secret_key='ConcursoProg'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://concursoprog_user:hola.123@localhost/ConcursoPro20207B'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#db = SQLAlchemy(app)
LoginManager = LoginManager()
LoginManager.init_app(app)
LoginManager.login_view='inicio'

@LoginManager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

@app.route('/')
def inicio():
    if current_user.is_authenticated:
        return render_template('Comun/Principal.html')
    else:
        return render_template('Index.html')

@app.route('/login',methods=['POST'])
def login():
    u=Usuario()
    u=u.validar(request.form['email'],request.form['password'])
    if u!=None:
        print(u.getTipo())
        login_user(u)
        return render_template('Comun/Principal.html')
    else:
        return 'Usuario invalido'
    #login_form = forms.LoginForm()
    #if request.method == 'POST' and login_form.validate():

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for("inicio"))
    else:
        abort(404)

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

#crud de registro de usuarios
@app.route('/usuarios/registro')
def registroUsuarios():
    return render_template('Usuarios/RegistroUsuarios.html')

@app.route('/usuarios/guardar',methods=['post'])
def guardarUsuario():
    u=Usuario()
    u.nombre = request.form['nombre']
    u.sexo = request.form['sexo']
    u.telefono = request.form['telefono']
    u.email = request.form['email']
    u.password = request.form['password']
    u.estatus = request.form['estatus']
    u.insertar()
    return redirect(url_for("inicio"))

@app.errorhandler(404)
def error_404(e):
    return render_template('Comun/Error.html',mensaje='Estamos resolviendo el problema'),404

@app.errorhandler(500)
def error_500(e):
    return render_template('Comun/Error.html',mensaje='Estamos resolviendo el problema'),500
if __name__ == '__main__':
 db.init_app(app)
 app.run(port = 3000, debug=True)