from _ast import alias
from symbol import return_stmt
#from typing import red
from flask import request
from Tools.scripts.make_ctype import method
from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db
from modelo.models import Categorias,Alumnos,PPropuestos,Docentes
from setuptools.command.alias import alias

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@cf0709-1415@localhost/ConcursoPro20207B'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#db = SQLAlchemy(app)

@app.route('/')
def Index():
    return  'Hello World'
#crud categorias
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


if __name__ == '__main__':
 db.init_app(app)

with app.app_context():
 #db.create_all()

 app.run(port = 3000, debug=True)