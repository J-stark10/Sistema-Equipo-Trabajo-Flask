from flask import Blueprint, request, render_template, redirect, url_for
from src.app import db
from src.tareas.models import Tarea

bp_tarea = Blueprint('tarea',__name__, template_folder='templates')

@bp_tarea.route('/')
def index():
    tareas = Tarea.query.all()

    return render_template('tarea/index.html', tareas=tareas)

@bp_tarea.route('/create', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        completada = True if 'completado' in request.form.keys() else False

        tarea = Tarea(descripcion=descripcion, completada=completada)
        db.session.add(tarea)
        db.session.commit()

        return redirect(url_for('tarea.index'))

    return render_template('tarea/create.html')

@bp_tarea.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    tarea = Tarea.query.get(id)

    if request.method == 'POST':
        tarea.descripcion = request.form['descripcion']
        tarea.completada = True if 'completado' in request.form.keys() else False

        db.session.commit()

        return redirect(url_for('tarea.index'))

    return render_template('tarea/edit.html', tarea=tarea)

@bp_tarea.route('/delete/<int:id>')
def delete(id):
    tarea = Tarea.query.get(id)
    db.session.delete(tarea)
    db.session.commit()

    return redirect(url_for('tarea.index'))