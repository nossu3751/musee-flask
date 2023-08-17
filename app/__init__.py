import os
from flask import Flask
from flask_cors import CORS
from .extensions import redis_wrapper, db
from app.api.demo.views import demo_blueprint
from dotenv import load_dotenv

origins = ["*"]

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app, origins=origins, supports_credentials=True)

    app.register_blueprint(demo_blueprint)

    redis_wrapper.init(
        host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT'),
        decode_responses=True
    )
    db.init_app(app)

    return app