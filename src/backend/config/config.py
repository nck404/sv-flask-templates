import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    # CORS allowed domains
    ALLOWED_DOMAINS = os.getenv('ALLOWED_DOMAINS', '').split(',') if os.getenv('ALLOWED_DOMAINS') else []
    
    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # SQLite specific configuration
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def get_cors_config():
        """Get CORS configuration for Flask"""
        return {
            'supports_credentials': True,
            'resources': {
                r"/*": {
                    'origins': Config.ALLOWED_DOMAINS
                }
            }
        }