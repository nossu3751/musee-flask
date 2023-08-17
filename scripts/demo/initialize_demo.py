import sys
sys.path.append(f'{sys.path[0]}/..')

from app import create_app
from app.extensions import redis_wrapper

def main():
    try:
        app = create_app()
        with app.app_context():
            ...
    except Exception:
        ...