import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    PROJECT_NAME = 'Car Price API'
    API_KEY = os.getenv('API_KEY','demo-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY','secret-key')
    JWT_ALGORITHM = 'HS256'
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhoat:6379')
    MODEL_PATH = 'app/models/model.joblib'


settings = Settings()
