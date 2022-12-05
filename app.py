from flask import Flask, render_template, url_for, request
import db
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

Session = sessionmaker(bind=db.engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lenguajes')
def lenguajes():
    datos = session.query(db.Lenguaje).all()
    return render_template('lenguajes.html', datos = datos)

@app.route('/proyectos', methods=['GET', 'POST'])
def proyectos():
    idProyecto = request.form.get('id')
    nombreProyecto = request.form.get('nombreproyecto')
    descripcionProyecto = request.form.get('descripcion')

    proyecto = db.Proyecto(idProyecto, nombreProyecto, descripcionProyecto)
    session.add(proyecto)
    session.commit()

    return render_template('proyectos.html')

if __name__ == '__main__':
    app.run(debug=True)