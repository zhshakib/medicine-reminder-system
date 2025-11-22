from flask import Flask, render_template
from app.database import init_db
from app.routes.auth_routes import auth_bp
from app.routes.dashboard_routes import dashboard_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'ADBHE!@!@ASMD'


    init_db()

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app
