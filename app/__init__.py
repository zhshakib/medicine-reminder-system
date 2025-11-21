from flask import Flask

from app.database import init_db

def create_app():
    app = Flask(__name__)


    init_db()

    @app.route('/')
    def index():
        return 'Hello, World!'
    
    return app
