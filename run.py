from src.app import create_app

app = create_app()

if (__name__) == '__main__':
    app.run(debug=True)


# 1. Establecer la variable de entorno para flask migrate: $env:FLASK_APP="run:flask_app"
# 2. Inicializar db : flask db init
# 3. Migrar : flask db migrate -m "Migracion inicial"
# 4. flask db upgrade