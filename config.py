import os
SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:professor9@localhost:5432/flashcard'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.urandom(64)