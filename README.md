# Flask App Factory + Blueprints

Este proyecto es una aplicación web construida con Flask usando el patrón App Factory y Blueprints. Está organizada para manejar al menos un módulo funcional de `miembros` con CRUD básico, además de una estructura para posibles otras secciones como `tareas`.

## Cómo se conecta todo

### `run.py`
- Es el punto de entrada de la aplicación.
- Importa `create_app` de `src.app` y crea la instancia de Flask.
- Ejecuta `flask_app.run(debug=True)` cuando se ejecuta directamente.
- Incluye comentarios sobre cómo usar `flask db` para migraciones.

### `src/app.py`
- Define la función `create_app()` que construye la aplicación Flask.
- Configura la base de datos SQLite con `SQLALCHEMY_DATABASE_URI = 'sqlite:///db_equipo.db'`.
- Inicializa `SQLAlchemy` y `Flask-Migrate`.
- Importa y registra los Blueprints:
  - `bp_core` de `src.core.routes` con prefijo `/`
  - `bp_miembro` de `src.miembros.routes` con prefijo `/miembros`
- Esta función es la columna vertebral que hace que el proyecto sea extensible.

### `src/__init__.py`
- Archivo de paquete vacío. Solo permite que Python trate `src` como un paquete importable.

### `src/core/routes.py`
- Define el Blueprint `bp_core` para la página principal.
- Solo contiene una ruta `/` que devuelve `core/index.html`.
- Se centra en mostrar la vista de inicio y los enlaces de navegación.

### `src/miembros/routes.py`
- Define el Blueprint `bp_miembro` para la sección de miembros.
- Contiene rutas para:
  - `/` listar miembros
  - `/create` crear nuevo miembro
  - `/edit/<int:id>` editar miembro existente
  - `/delete/<int:id>` eliminar miembro
- Usa el modelo `Miembro` y `db` desde `src.app`.
- Gestiona formularios HTML con métodos `POST` y `GET`.

### `src/miembros/models.py`
- Define el modelo `Miembro` con SQLAlchemy.
- La tabla se llama `miembros` y tiene campos:
  - `id` (clave primaria)
  - `nombre` (texto obligatorio)
  - `email` (texto obligatorio)
- Representación simple con `__repr__` para debugging.

### Templates principales
- `src/templates/base.html`
  - Plantilla base con estructura HTML y Tailwind CSS.
  - Contiene bloques `title` y `content` para extender.
- `src/core/templates/core/index.html`
  - Página de inicio con barra de navegación.
  - Enlaces a `Inicio` y `Miembro`.
- `src/miembros/templates/miembro/index.html`
  - Lista de miembros en una tabla.
  - Botones para editar y eliminar cada miembro.
- `src/miembros/templates/miembro/create.html`
  - Formulario para crear un nuevo miembro.
- `src/miembros/templates/miembro/edit.html`
  - Formulario para editar un miembro existente.

### `migrations/`
- Contiene la configuración de `Flask-Migrate` y Alembic.
- `alembic.ini` y `env.py` gestionan la conexión de migración.
- `migrations/versions/350d0280f616_migracion_inicial.py` es la migración inicial.

### `requirements.txt`
- Lista las dependencias necesarias para ejecutar el proyecto.
- Sirve para reconstruir el entorno con `pip install -r requirements.txt`.

### `env/`
- Entorno virtual local de Python.
- Contiene dependencias instaladas.
- No es necesario modificarlo para entender la lógica de la aplicación.

## Estado del proyecto

- El módulo `miembros` está funcionando con CRUD completo.
- El módulo `tareas` existe como carpeta, pero actualmente está vacío en `src/tareas/routes.py` y `src/tareas/models.py`.
- Se usa una base de datos SQLite local: `db_equipo.db`.

## Instrucciones básicas para correr

1. Activar el entorno virtual.
2. Ejecutar `python run.py`.
3. Abrir el navegador en `http://127.0.0.1:5000/`.

### Migraciones con Flask-Migrate

- Establecer variable de entorno:
  - Windows PowerShell: `$env:FLASK_APP="run:flask_app"`
- Inicializar migraciones:
  - `flask db init`
- Crear migración:
  - `flask db migrate -m "Migracion inicial"`
- Aplicar migración:
  - `flask db upgrade`

## Árbol de archivos del proyecto

```
10-App-Factory-Migrate-Flask/
├─ README.md
├─ requirements.txt
├─ run.py
├─ env/                # entorno virtual local
├─ instance/           # carpeta de instancia (configuraciones opcionales)
├─ migrations/
│  ├─ alembic.ini
│  ├─ env.py
│  ├─ README
│  ├─ script.py.mako
│  └─ versions/
│     └─ 350d0280f616_migracion_inicial.py
└─ src/
   ├─ __init__.py
   ├─ app.py
   ├─ core/
   │  ├─ __init__.py
   │  ├─ routes.py
   │  └─ templates/
   │     └─ core/
   │        └─ index.html
   ├─ miembros/
   │  ├─ __init__.py
   │  ├─ models.py
   │  ├─ routes.py
   │  └─ templates/
   │     └─ miembro/
   │        ├─ index.html
   │        ├─ create.html
   │        └─ edit.html
   ├─ tareas/
   │  ├─ __init__.py
   │  ├─ models.py
   │  └─ routes.py
   └─ templates/
      └─ base.html
```

> Nota: el árbol omite los archivos del entorno virtual (`env/Lib/site-packages`) para mantenerlo claro y centrado en el código fuente del proyecto.
