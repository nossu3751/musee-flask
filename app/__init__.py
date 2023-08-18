import os
from flask import Flask
from flask_cors import CORS
from .extensions import redis_wrapper, db
from app.api.demo.views import demo_blueprint
from dotenv import load_dotenv
from config import Config

origins = ["*"]

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=origins, supports_credentials=True)

    app.register_blueprint(demo_blueprint)

    db.init_app(app)

    return app