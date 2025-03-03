# importar class
from flask import Flask, redirect, render_template, session, url_for
import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# importar modulos de rutas
from routes.pagos_route import pagos_bp
from routes.index_route import index_bp
from routes.login_route import login_bp
from routes.menu_route import menu_bp
from routes.duenos_route import duenos_bp
from routes.inquilinos_route import inquilinos_bp
from routes.puestos_route import puestos_bp
from routes.contratos_route import contratos_bp
from routes.egresos_route import egresos_bp

from routes.deudas_secre_route import deudas_secre_bp
from routes.egresos_secre_route import egresos_secre_bp
from routes.pagos_secre_route import pagos_secre_bp

# para clinica
from routes.consultas_route import consultas_bp

from routes.doctor_route import doctor_bp

from routes.asignar_consultorios_route import asignar_consultorios_bp

from routes.reportes_routes import reportes_bp

from routes.consultorios_route import consultorios_bp


# inicializar aplicacion
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey123")  # Cambia esto por una clave segura

# Registrar Blueprints (módulos de rutas)
app.register_blueprint(pagos_bp)
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(duenos_bp)
app.register_blueprint(inquilinos_bp)
app.register_blueprint(puestos_bp)
app.register_blueprint(contratos_bp)
app.register_blueprint(egresos_bp)

app.register_blueprint(deudas_secre_bp)
app.register_blueprint(egresos_secre_bp)
app.register_blueprint(pagos_secre_bp)

# para clinica
app.register_blueprint(consultas_bp)

app.register_blueprint(doctor_bp)

app.register_blueprint(asignar_consultorios_bp)

app.register_blueprint(reportes_bp)

app.register_blueprint(consultorios_bp)


# Context processor para compartir el rol de usuario en todas las plantillas
@app.context_processor
def agregar_contexto_global():
      return {
            'usuario': session.get('usuario'),
            'rol': session.get('rol')
      }



# comprobar si se encuentra en el archivo inicial
if __name__ == '__main__':
      # lanzar aplicacion
      app.run(
            # habilitar modo depuracion
            debug = True,
            # modificar el puerto
            port=int(os.getenv("FLASK_RUN_PORT", 5000)),
            host=os.getenv("FLASK_RUN_HOST", "127.0.0.1")
      )
