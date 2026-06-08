from flask import render_template, redirect, url_for, request, Blueprint

from src.app import db
from src.miembros.models import Miembro

bp_miembro = Blueprint('miembro', __name__, template_folder='templates')

@bp_miembro.route('/')
def index():
    miembros = Miembro.query.all()

    return render_template('miembro/index.html', miembros=miembros)


@bp_miembro.route('/create',methods=['POST','GET'])
def create():

    if request.method == 'POST':

        nombre = request.form['nombre']
        email = request.form['email']

        miembro = Miembro(nombre=nombre, email=email)
        db.session.add(miembro)
        db.session.commit()
        
        return redirect(url_for('miembro.index'))

    return render_template('miembro/create.html')

@bp_miembro.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    miembro = Miembro.query.get(id)

    if request.method == 'POST':

        miembro.nombre = request.form.get('nombre')
        miembro.email = request.form.get('email')

        db.session.commit()

        return redirect(url_for('miembro.index'))
    return render_template('miembro/edit.html', miembro=miembro)

@bp_miembro.route('/delete/<int:id>')
def delete(id):
    miembro = Miembro.query.get(id)
    db.session.delete(miembro)

    db.session.commit()

    return redirect(url_for('miembro.index'))
