#from urllib import request
#from Tools.scripts.make_ctype import method
#from crypt import methods
from functools import partial
from operator import eq

from flask import Flask, render_template,abort,request, redirect,url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

from modelo.models import db, Categorias, Usuario, Alumnos,PPropuestos,Docentes,Carreras, Equipos, Ediciones, problemasResueltos
from modelo.models import db, Categorias, Usuario, Alumnos,Docentes,BancoProblemas,ProblemasPropuestos
import json

app = Flask(__name__)
app.secret_key='ConcursoProg'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@cf0709-1415@localhost/ConcursoPro20207B'
#app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#db = SQLAlchemy(app)
loginManager=LoginManager()
loginManager.init_app(app)
loginManager.login_view='inicio'

@loginManager.user_loader
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
    u=u.validar(request.form['email'],request.form['password_hash'])
    if u!=None:
        print(u.getTipo())
        login_user(u)
        return render_template('/Comun/Principal.html')
    else:
        return 'Usuario invalido'

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

@app.route('/Comun/Principal.html')
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
@login_required
def nuevoAlumno():
    return render_template('Alumnos/nuevoAlumno.html')
@app.route('/alumnos/eliminar/<int:noControl>') #ELIMINAR ALUMNO
@login_required
def eliminarAlumno(noControl):
    alucno=Alumnos()
    alucno.noControl = noControl
    alucno.eliminar()
    return redirect(url_for('consultaGeneralAlumnos'))
@app.route('/alumnos/guardar', methods=['POST']) #GUARDAR ALUMNO
@login_required
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

#@app.route('/Alumnos')
#@login_required
@app.route('/Alumnos') #CONSULTA GENERAL
@login_required
def consultaGeneralAlumnos():
    alucnos = Alumnos()
    alucnosGeneral = alucnos.consultaGeneral()
    return render_template('Alumnos/consultaGeneral.html',alucnosGeneral=alucnosGeneral)
@app.route('/alumnos/<int:noControl>')
@login_required
def consultarAlumno(noControl): #CONSULTA INDIVIDUAL
    alucnos = Alumnos()
    alucnos.noControl=noControl
    alucnos = alucnos.consultaIndividual()
    return render_template('Alumnos/editarAlumno.html',alucnos=alucnos)
@app.route('/alumnos/modificar', methods = ['POST'])
@login_required
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

#INICIO CRUD PROBLEMASPROPUESTOS
@app.route('/ppropuestos/new') #AÑADIR ALUMNO
def nuevoPP():
    return render_template('problemasPropuestos/nuevoProblemaP.html')
@app.route('/ppropuestos/eliminar/<int:idProPue>') #ELIMINAR ALUMNO
def eliminarPP(idProPue):
    pp = ProblemasPropuestos()
    pp.idProPue = idProPue
    pp.eliminar()
    return redirect(url_for('consultaGeneralPPropuestos'))
@app.route('/ppropuestos/guardar', methods=['POST']) #GUARDAR ALUMNO
def guardarPP():
    pp = ProblemasPropuestos()
    pp.idProPue=request.form ['idProPue']
    pp.globo=request.form ['globo']
    pp.idProblema=request.form ['idProblema']
    pp.idEdicion=request.form ['idEdicion']
    pp.idCategoria=request.form ['idCategoria']
    pp.insertar()
    return redirect(url_for('consultaGeneralPPropuestos'))
@app.route('/PPropue') #CONSULTA GENERAL
def consultaGeneralPPropuestos():
    pp = ProblemasPropuestos()
    ppGeneral = pp.consultaGeneral()
    return render_template('problemasPropuestos/consultaGeneral.html',ppGeneral=ppGeneral)
@app.route('/ppropuestos/<int:idProPue>')
def consultarPP(idProPue): #CONSULTA INDIVIDUAL
    pp = ProblemasPropuestos()
    pp.idProPue=idProPue
    pp = pp.consultaIndividual()
    return render_template('problemasPropuestos/editarPP.html',pp=pp)
@app.route('/ppropuestos/modificar', methods = ['POST'])
def actualizarPP(): #ACTUALIZAR ALUMNOS
    pp = ProblemasPropuestos()
    pp.idProPue=request.form ['idProPue']
    pp.globo=request.form ['globo']
    pp.idProblema=request.form ['idProblema']
    pp.idEdicion=request.form ['idEdicion']
    pp.idCategoria=request.form ['idCategoria']
    pp.actualizar()
    return redirect(url_for('consultaGeneralPPropuestos'))
#FIN CRUD PROBLEMASPROPUESTOS

#INICIO CRUD BANCO PROBLEMAS
@app.route('/bproblemas/new') #AÑADIR ALUMNO
def nuevoProblema():
    return render_template('bancoProblemas/nuevoProblema.html')
@app.route('/bproblemas/eliminar/<int:idProblema>') #ELIMINAR ALUMNO
def eliminarProblema(idProblema):
    problemas = BancoProblemas()
    problemas.idProblema = idProblema
    problemas.eliminar()
    return redirect(url_for('consultaGeneralProblemas'))
@app.route('/bproblemas/guardar', methods=['POST']) #GUARDAR ALUMNO
def guardarProblemas():
    problemas = BancoProblemas()
    problemas.idProblema=request.form ['idProblema']
    problemas.nombre=request.form ['nombre']
    problemas.puntos=request.form ['puntos']
    problemas.tiempoMaximo=request.form ['tiempoMaximo']
    problemas.descripcion=request.form ['descripcion']
    problemas.insertar()
    return redirect(url_for('consultaGeneralProblemas'))
@app.route('/Problemas') #CONSULTA GENERAL
def consultaGeneralProblemas():
    problemas = BancoProblemas()
    problemasGeneral = problemas.consultaGeneral()
    return render_template('bancoProblemas/problemasGeneral.html',problemasGeneral=problemasGeneral)
@app.route('/bproblemas/<int:idProblema>')
def consultarProblema(idProblema): #CONSULTA INDIVIDUAL
    problemas = BancoProblemas()
    problemas.idProblema=idProblema
    problemas = problemas.consultaIndividual()
    return render_template('bancoProblemas/editarProblema.html',problemas=problemas)
@app.route('/bproblemas/modificar', methods = ['POST'])
def actualizarProblema(): #ACTUALIZAR ALUMNOS
    problemas = BancoProblemas()
    problemas.idProblema=request.form ['idProblema']
    problemas.nombre=request.form ['nombre']
    problemas.puntos=request.form ['puntos']
    problemas.tiempoMaximo=request.form ['tiempoMaximo']
    problemas.descripcion=request.form ['descripcion']
    problemas.actualizar()
    return redirect(url_for('consultaGeneralProblemas'))
#FIN BANCO PROBLEMAS

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
@login_required
def consultaGeneralCategorias():
    category = Categorias()
    categoryGeneral = category.consultaGeneral()
    return render_template('Categorias/consultaGeneral.html',categoryGeneral=categoryGeneral)
@app.route('/categorias/guardar', methods=['POST'])
@login_required
def guardarCategoria():
    category = Categorias()
    category.idProPue = request.form['idProPue']
    category.idCategoria = request.form ['idCategoria']
    category.nombre = request.form['nombre']
    category.semestreLimite = request.form['semestreLimite']
    category.insertar()
    return redirect(url_for('consultaGeneralCategorias'))
@app.route('/categorias/eliminar/<int:idCategoria>') #ELIMINAR ALUMNO
@login_required
def eliminarCategoria(idCategoria):
    category = Categorias()
    category.idCategoria = idCategoria
    category.eliminar()
    return redirect(url_for('consultaGeneralCategorias'))
@app.route('/categorias/modificar', methods = ['POST'])
@login_required
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
@login_required
def eliminarDocente(idDocente):
    docentis = Docentes()
    docentis.idDocente = idDocente
    docentis.eliminar()
    return redirect(url_for('consultaGeneralDocentes'))
@app.route('/docentes/new') #AÑADIR ALUMNO
@login_required
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

#curd de Carrera
@app.route('/carrera/new')#añadir carrera
#@login_required
def nuevaCarrera():
    return render_template('Carrera/nuevaCarrera.html')
@app.route('/carrera/eliminar/<int:idCarrera>')#eliminar carrera
def eliminarCarrera(idCarrera):
    ca=Carreras()
    ca.idCarrera = idCarrera
    ca.eliminar()
    return redirect(url_for('consultaGeneralCarreras'))
@app.route('/carrera/guardar',methods=['POST'])#guardar carrera
def guardarCarrera():
     ca=Carreras()
     ca.idCarrera = request.form['idCarrera']
     ca.noControl = request.form['noControl']
     ca.nombre = request.form['nombre']
     ca.siglas = request.form['siglas']
     ca.insertar()
     return redirect(url_for('consultaGeneralCarreras'))
@app.route('/Carreras') #CONSULTA GENERAL
def consultaGeneralCarreras():
    ca = Carreras()
    caGeneral = ca.consultaGeneral()
    return render_template('Carrera/consultaGeneral.html',caGeneral=caGeneral)
@app.route('/carrera/<int:idCarrera>')#consulta individual
def  consultaCarrera(idCarrera):
    ca=Carreras()
    ca.idCarrera = idCarrera
    ca = ca.consultaIndividual()
    return render_template('Carrera/editarCarrera.html',ca=ca)
@app.route('/carrera/modificar',methods=['POST'])#actualizar Carrera
def actualizarCarrera():
     ca.idCarrera = request.form['idCarrera']
     ca.noControl = request.form['noControl']
     ca.nombre = request.form['nombre']
     ca.siglas = request.form['siglas']
     ca.actualizar()
     return redirect(url_for('consultaGeneralCarreras'))
#fin Crud Carrera

#inicio CRUD de equipos
@app.route('/equipos/new')#añadir equipo
@login_required
def nuevoEquipo():
    return render_template('Equipos/nuevoEquipo.html')
@app.route('/equipos/eliminar/<int:idEquipo>')#eliminar equipo
def eliminarEquipo(idEquipo):
    eq=Equipos
    eq.idEqipo = idEquipo
    eq.eliminar()
    return redirect(url_for('consultaGeneralEquipos'))
@app.route('/equipos/guardar', methods=['POST'])#guardar equipo
@login_required
def guardarEquipos():
    eq=Equipos()
    eq.idEqipo = request.form['idEquipo']
    eq.ProRes = request.form['ProRes']
    eq.ProPue = request.form['ProPue']
    eq.nombre = request.form['nombre']
    eq.noControl1 = request.form['noControl1']
    eq.noControl2 = request.form['noControl2']
    eq.noControl3 = request.form['noControl3']
    eq.idDocentes = request.form['idDocentes']
    eq.idCategorias = request.form['idCarreras']
    eq.insertar()
    return redirect(url_for('consultaGeneralEquipos'))
@app.route('/Equipos')#consulta general
@login_required
def consultaGeneralEquipos():
    eq=Equipos()
    eqGeneral = eq.consultaGeneral()
    return render_template('/Equipos/consultaGeneral.html',eqGeneral=eqGeneral)
@app.route('/equipos/<int:idEquipos>')#consulta individual
@login_required
def consultaEquipos(idEquipo):
    eq =Equipos()
    eq.idEqipo=idEquipo
    eq= eq.consultaIndividual()
    return render_template('Equipos/editarEquipo.html',eq=eq)
@app.route('/equipos/modificar',methods=['POST']) #actualizar equipos
def actualizarEquipos():
    eq = Equipos()
    eq.idEqipo = request.form['idEquipo']
    eq.ProRes = request.form['ProRes']
    eq.ProPue = request.form['ProPue']
    eq.nombre = request.form['nombre']
    eq.noControl1 = request.form['noControl1']
    eq.noControl2 = request.form['noControl2']
    eq.noControl3 = request.form['noControl3']
    eq.idDocentes = request.form['idDocentes']
    eq.idCategorias = request.form['idCarreras']
    eq.actualizar()
    return redirect(url_for('consultaGeneralEquipos'))
#fin del Crud

#inicio CRUD Ediciones
@app.route('/ediciones/new')#añadir edicion
def nuevaEdicion():
    return render_template('Ediciones/nuevaEdicion.html')
@app.route('/ediciones/eliminar/<int:idEdicion>')#eliminar ediciones
def eliminarEdiciones():
    edi = Ediciones()
    edi.idEdicion = idEdicion
    edi.eliminar()
    return redirect(url_for('consultaGeneralEdiciones'))
@app.route('/ediciones/guardar',methods=['POST'])
def guardarEdiciones():
    edi = Ediciones()
    edi.idEdicion = request.form['idEdicion']
    edi.idProPue = request.form['idProPue']
    edi.ProRes = request.form['idProRes']
    edi.nombre = request.form['nombre']
    edi.fechaRegistro = request.form['fechaRegistro']
    edi.fechaEvento = request.form['fechaEvento']
    edi.insertar()
    return redirect(url_for('consultaGeneralEdiciones'))
@app.route('/Ediciones')#consulta general
def consultaGeneralGeneral():
    edi = Ediciones()
    ediGeneral=edi.consultaGeneral()
    return render_template('Ediciones/consultaGeneral.html',ediGeneral=ediGeneral)
@app.route('/ediciones/<int:idEdicion>')#consultar individual
def consultaEdicion(idEdicion):
    edi=Ediciones()
    edi.idEdicion = idEdicion
    edi = edi.consultaIndividual()
    return render_template('Ediciones/editarEdicion.html',edi=edi)
@app.route('/edicion/modificar',methods=['POST'])#actualizar ediciones
def actualizarEdicion():
    edi = Ediciones()
    edi.idEdicion = request.form['idEdicion']
    edi.idProPue = request.form['idProPue']
    edi.ProRes = request.form['idProRes']
    edi.nombre = request.form['nombre']
    edi.fechaRegistro = request.form['fechaRegistro']
    edi.fechaEvento = request.form['fechaEvento']
    edi.actualizar()
    return redirect(url_for('consultaGeneralEdiciones'))
#FIN CRUD CARRERA

#Inicio Crud problemasResueltos
@app.route('/probRes/new')#añadir problemasResueltos
def nuevoproblemasResueltos():
    return render_template('ProResueltos/nuevaProResueltos.html')
@app.route('/proResu/eliminar/<int:idProRes>')#eliminar ProResu
def eliminarproRes(idProRes):
    pro=ProRes()
    pro.idProRes = idProRes
    pro.eliminar()
    return redirect(url_for('consultaGeneralProResueltos'))
@app.route('/probRes/guardar',methods=['post'])#guardar proRes
def guardarproRes():
    pro = ProRes()
    pro.idProRes = request.form['idProRes']
    pro.idProPue = request.form['idProPue']
    pro.idEquipo = request.form['idEquipo']
    pro.tiempo = request.form['tiempo']
    pro.tiempoEjecucion = request.form['tiempoEjecucion']
    pro.puntaje = request.form['puntaje']
    pro.insertar()
    return redirect(url_for('consultaGeneralProResueltos'))
@app.route('/ProResueltos')#consulta general
def consultarproRes():
    pro=ProRes()
    proGeneral = pro.consultaGeneral()
    return render_template('ProResueltos/consultaGeneral.html',proGeneral=proGeneral)
@app.route('/proResu/<int:idProRes>')#consultaindividual
def consultaproRes(idProRes):
    pro=ProRes()
    pro.idProRes = idProRes
    pro= pro.consultaIndividual()
    return render_template('ProResueltos/editarProResueltos.html',pro=pro)
@app.route('/probRes/modificar',methods=['post'])#actualizat proRes
def actualizarproRes():
    pro = ProRes()
    pro.idProRes = request.form['idProRes']
    pro.idProPue = request.form['idProPue']
    pro.idEquipo = request.form['idEquipo']
    pro.tiempo = request.form['tiempo']
    pro.tiempoEjecucion = request.form['tiempoEjecucion']
    pro.puntaje = request.form['puntaje']
    pro.actualizar()
    return redirect(url_for('consultaGeneralProResueltos'))
#fin crud proresueltos

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
    u.tipo = request.form['tipo']
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
 app.run(debug=True)
#with app.app_context():
 #db.create_all()
