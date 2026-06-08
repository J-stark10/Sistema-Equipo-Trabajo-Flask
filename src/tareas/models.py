from src.app import db

class Tarea(db.Model):
    __tablename__ = 'tareas'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String, nullable=False)
    completada = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Tarea : descripcion {self.descripcion} - completada {self.completada}>'
    
    