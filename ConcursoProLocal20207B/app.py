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
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
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
        return render_template('Alumnos/consultaGeneral.html')
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

#INICIO CRUD alumnos FUNCIONANDO
@app.route('/alumnos/new') #AÑADIR ALUMNO
def nuevoAlumno():
    return render_template('Alumnos/nuevoAlumno.html')
@app.route('/alumnos/eliminar/<int:noControl>') #ELIMINAR ALUMNO
def eliminarAlumno(noControl):
    alucno=Alumnos()
    alucno.noControl = noControl
    alucno.eliminar()
    return redirect(url_for('consultaGeneralAlumnos'))
@app.route('/alumnos/guardar', methods=['POST']) #GUARDAR ALUMNO
def guardarAlumno():
    alucnos=Alumnos()
    alucnos.noControl=request.form ['noControl']
    alucnos.semestre=request.form ['semestre']
    alucnos.idUsuario=request.form ['idUsuario']
    alucnos.idCarrera=request.form ['idCarrera']
    alucnos.idProRes=request.form ['idProRes']
    alucnos.insertar()
    return redirect(url_for('consultaGeneralAlumnos'))
@app.route('/Alumnos') #CONSULTA GENERAL
def consultaGeneralAlumnos():
    alucnos = Alumnos()
    alucnosGeneral = alucnos.consultaGeneral()
    return render_template('Alumnos/consultaGeneral.html',alucnosGeneral=alucnosGeneral)
@app.route('/alumnos/<int:noControl>')
def consultarAlumno(noControl): #CONSULTA INDIVIDUAL
    alucnos = Alumnos()
    alucnos.noControl=noControl
    alucnos = alucnos.consultaIndividual()
    return render_template('Alumnos/editarAlumno.html',alucnos=alucnos)
@app.route('/alumnos/modificar', methods = ['POST'])
def actualizarAlumno(): #ACTUALIZAR ALUMNOS
    alucnos = Alumnos()
    alucnos.noControl=request.form['noControl']
    alucnos.semestre=request.form['semestre']
    alucnos.idUsuario=request.form['idUsuario']
    alucnos.idCarrera=request.form['idCarrera']
    alucnos.idProRes=request.form['idProRes']
    alucnos.actualizar()
    return redirect(url_for('consultaGeneralAlumnos'))
#FIN CRUD ALUMNOS FUNCIONANDO

#INICIO CRUD CATEGORIAS WORKING
@app.route('/categorias/<int:idCategoria>')
def consultarCategoria(idCategoria): #CONSULTA INDIVIDUAL
    category = Categorias()
    category.idCategoria=idCategoria
    category = category.consultaIndividual()
    return render_template('Categorias/editarCategoria.html',category=category)
@app.route('/categorias/new') #AÑADIR ALUMNO
def nuevoCategoria():
    return render_template('Categorias/nuevaCategoria.html')
@app.route('/Categorias')
def consultaGeneralCategorias():
    category = Categorias()
    categoryGeneral = category.consultaGeneral()
    return render_template('Categorias/consultaGeneral.html',categoryGeneral=categoryGeneral)
@app.route('/categorias/guardar', methods=['POST'])
def guardarCategoria():
    category = Categorias()
    category.idProPue = request.form['idProPue']
    category.idCategoria = request.form ['idCategoria']
    category.nombre = request.form['nombre']
    category.semestreLimite = request.form['semestreLimite']
    category.insertar()
    return redirect(url_for('consultaGeneralCategorias'))
@app.route('/categorias/eliminar/<int:idCategoria>') #ELIMINAR ALUMNO
def eliminarCategoria(idCategoria):
    category = Categorias()
    category.idCategoria = idCategoria
    category.eliminar()
    return redirect(url_for('consultaGeneralCategorias'))
@app.route('/categorias/modificar', methods = ['POST'])
def actualizarCategoria(): #ACTUALIZAR ALUMNOS
    category = Categorias()
    category.idProPue = request.form['idProPue']
    category.idCategoria = request.form ['idCategoria']
    category.nombre = request.form['nombre']
    category.semestreLimite = request.form['semestreLimite']
    category.actualizar()
    return redirect(url_for('consultaGeneralCategorias'))
#FIN CRUD CATEGORIAS

#INICIO CRUD DOCENTES
@app.route('/docentes/<int:idDocente>')
def consultarDocente(idDocente): #CONSULTA INDIVIDUAL
    docentis = Docentes()
    docentis.idDocente=idDocente
    docentis = docentis.consultaIndividual()
    return render_template('Docentes/editarDocente.html',docentis=docentis)
@app.route('/docentes/modificar', methods = ['POST'])
def actualizarDocente(): #ACTUALIZAR ALUMNOS
    docentis = Docentes()
    docentis.idDocente = request.form['idDocente']
    docentis.escolaridad = request.form ['escolaridad']
    docentis.especialidad = request.form['especialidad']
    docentis.cedula = request.form['cedula']
    docentis.idCarrera = request.form['idCarrera']
    docentis.idUsuario = request.form['idUsuario']
    docentis.noControl = request.form['noControl']
    docentis.actualizar()
    return redirect(url_for('consultaGeneralDocentes'))
@app.route('/docentes/eliminar/<int:idDocente>') #ELIMINAR ALUMNO
def eliminarDocente(idDocente):
    docentis = Docentes()
    docentis.idDocente = idDocente
    docentis.eliminar()
    return redirect(url_for('consultaGeneralDocentes'))
@app.route('/docentes/new') #AÑADIR ALUMNO
def nuevoDocente():
    return render_template('Docentes/nuevoDocentes.html')
@app.route('/Docentes')
def consultaGeneralDocentes():
    docentis = Docentes()
    docentisyGeneral = docentis.consultaGeneral()
    return render_template('Docentes/consultaGeneral.html',docentisyGeneral=docentisyGeneral)
@app.route('/docentes/guardar', methods=['POST'])
def guardarDocentes():
    docentis = Docentes()
    docentis.idDocente = request.form['idDocente']
    docentis.escolaridad = request.form ['escolaridad']
    docentis.especialidad = request.form['especialidad']
    docentis.cedula = request.form['cedula']
    docentis.idCarrera = request.form['idCarrera']
    docentis.idUsuario = request.form['idUsuario']
    docentis.noControl = request.form['noControl']
    docentis.insertar()
    return redirect(url_for('consultaGeneralDocentes'))
#FIN CRUD DOCENTES





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
 app.run(port=3000, debug=True)
#with app.app_context():
 #db.create_all()
