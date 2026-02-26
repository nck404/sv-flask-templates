from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from routes.auth import auth_bp
from routes.lessons import lessons_bp
from routes.blog import blog_bp
from config.config import Config

app = Flask(__name__)

# Set CORS configuration with fallback for empty domains
cors_config = Config.get_cors_config()
if not cors_config['resources']['r"/*']['origins']:
    cors_config['resources']['r"/*']['origins'] = ['http://localhost:3000', 'http://127.0.0.1:3000', 'http://localhost:5173', 'http://localhost:8080']
CORS(app, **cors_config)

# Set database configuration with fallback
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI or 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS or False
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY or 'super-secret'

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(lessons_bp, url_prefix='/')


@app.route('/')
def index():
    return {"msg": "API is running"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
