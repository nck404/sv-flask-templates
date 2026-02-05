import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from routes.auth import auth_bp
from routes.lessons import lessons_bp
from routes.blog import blog_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True,
    resources={
        r"/*": {
            "origins": [
                "http://localhost:3000",
                "http://127.0.0.1:3000",
                "http://localhost:5173",
                "http://localhost:8080"
            ]
        }
    }
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(lessons_bp, url_prefix='/')
app.register_blueprint(blog_bp, url_prefix='/api/blog')


@app.route('/')
def index():
    return {"msg": "API is running"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
