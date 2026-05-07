# Aplicación de Gestión de Empleados (Modo Oscuro)

Aplicación web pequeña con FastAPI + Jinja2 que permite registrar empleados (nombre, apellido, DNI, cargo) usando SQLite.

Requisitos:
- Python 3.8+
- Instalar dependencias:
  pip install -r requirements.txt

Ejecutar:
  uvicorn main:app --reload --host 0.0.0.0 --port 8000
o
  python main.py

Abrir http://localhost:8000 en el navegador. La base de datos se crea en ./app.db.