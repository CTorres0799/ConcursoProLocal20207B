#from urllib import request
#from Tools.scripts.make_ctype import method
from flask import Flask, render_template, request, abort, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Categorias, Usuario, Alumnos,PPropuestos,Docentes
import json

app = Flask(__name__)
app.secret_key='ConcursoProg'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:CruzYPedro523@localhost/ConcursoPro20207B'

from _ast import alias
from symbol import return_stmt
#from typing import red
from flask import request
from Tools.scripts.make_ctype import method
from flask import Flask, render_template,redirect,url_for
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db
from modelo.models import Categorias,Alumnos,PPropuestos,Docentes
from setuptools.command.alias import alias


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@cf0709-1415@localhost/ConcursoPro20207B'
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

#mysql = MYSQL(app)
#app.secret_key = '123'

@app.route('/')
def Index():
    return  'Hello World'
#crud categorias
def index():
    return  render_template('index.html')

#@app.route('/add contact', method=['POST'])
#def add_contact():
    #if request.method == 'POST':
     #   Usuario = request.form['Usuario']
      #  password = request.form['password']
     

#@app.route('/login', methods =['GET','POST'])
#def login():
 #   login_form = forms.LoginForm()
  #  if request.method == 'POST' and login_form.validate():
   #     pass
    #return render_template('Index.html', form = login_form)


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
@app.route('/categorias/guardar',methods=['POST'])
def guardarCategoria():
 categorias=Categorias()
 categorias.Nombre=request.form['nombre']
 categorias.SemestreLimite=request.form['semestreLimite']
 categorias.idProPue=request.form['idProPue']
 categorias.insertar()
 return 'Categoria Registrada con Exito'
#final

#INICIO CRUD alumnos FUNCIONANDO
@app.route('/alumnos/new')
def nuevoAlumno():
    return render_template('Alumnos/nuevoAlumno.html')
@app.route('/alumnos/eliminar/<int:noControl>')
def eliminarAlumno(noControl):
    alucno=Alumnos()
    alucno.noControl = noControl
    alucno.eliminar()
    return redirect(url_for('consultaGeneralAlumnos'))
@app.route('/alumnos/guardar', methods=['POST'])
def guardarAlumno():
    alucnos=Alumnos()
    alucnos.noControl=request.form ['noControl']
    alucnos.semestre=request.form ['semestre']
    alucnos.idUsuario=request.form ['idUsuario']
    alucnos.idCarrera=request.form ['idCarrera']
    alucnos.idProRes=request.form ['idProRes']
    alucnos.insertar()
    return redirect(url_for('consultaGeneralAlumnos'))
@app.route('/Alumnos')
def consultaGeneralAlumnos():
    alucnos = Alumnos()
    alucnosGeneral = alucnos.consultaGeneral()
    return render_template('Alumnos/consultaGeneral.html',alucnosGeneral=alucnosGeneral)
@app.route('/alumnos/<int:noControl>')
def consultarAlumno(noControl):
    alucnos = Alumnos()
    alucnos.noControl=noControl
    alucnos = alucnos.consultaIndividual()
    return render_template('Alumnos/editarAlumno.html',alucnos=alucnos)
@app.route('/alumnos/modificar', methods = ['POST'])
def actualizarAlumno():
    alucnos = Alumnos()
    alucnos.noControl=request.form['noControl']
    alucnos.semestre=request.form['semestre']
    alucnos.idUsuario=request.form['idUsuario']
    alucnos.idCarrera=request.form['idCarrera']
    alucnos.idProRes=request.form['idProRes']
    alucnos.actualizar()
    return redirect(url_for('consultaGeneralAlumnos'))
#FIN CRUD ALUMNOS FUNCIONANDO

#crud ProblemasPropuestos
@app.route('/pp/new')
def nuevoPP():
    return render_template('problemasPropuestos/nuevoPP.html')
@app.route('/pp/guardar', methods=['POST'])
def guardarPP():
    pp = PPropuestos()
    pp.idProPue=request.form['']
    pp.globo.form['']
    pp.idProblema.form['']
    pp.idEdicion.form['']
    pp.idCategoria.fomr['']
    pp.insertar()
    return 'Problema propuesto Añadido correctamente'
#final
#crud Docentes
@app.route('/docentes/new')
def nuevoDocente():
    return render_template('Docentes/nuevoDocentes.html')
@app.route('/docentes/guardar', methods=['POST'])
def guardarDocente():
    docente = Docentes()
    docente.idDocente = request.form['idDocente']
    docente.escolaridad = request.form['escolaridad']
    docente.especialidad = request.form['especialidad']
    docente.cedula = request.form['cedula']
    docente.idCarrera = request.form['idCarrera']
    docente.idUsuario = request.form['idUsuario']
    docente.noControl = request.fomr['noControl']
    docente.insert()
    return 'Docentes agregado con exito'
#final


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

with app.app_context():
 #db.create_all()

 app.run(port = 3000, debug=True)