import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///cotacao.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False