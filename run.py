from app import create_app
import os
os.umask(0o002)

app = create_app()
debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)