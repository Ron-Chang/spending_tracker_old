from flask_compress import Compress
from app import create_app


app = create_app()
Compress(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
