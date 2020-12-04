from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://concursoprog_user:hola.123@localhost/concursopro20207b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

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

if __name__ == '__main__':
 app.run(port = 3000, debug=True)