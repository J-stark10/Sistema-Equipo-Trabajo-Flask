from src.app import db

class Miembro(db.Model):
    __tablename__ = 'miembros'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Miembro : Nombre {self.nombre} Email {self.email}>'