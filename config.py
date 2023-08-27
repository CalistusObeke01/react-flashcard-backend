import os
SECRET_KEY = os.urandom(32)

# SQLALCHEMY_DATABASE_URI = 'postgresql://react_flashcard_db_user:1Dq3GrKGaW0hqtBspNLMOaPiaLa4AZed@dpg-cggo1l9mbg5e1o04gj20-a.oregon-postgres.render.com/react_flashcard_db'
SQLALCHEMY_DATABASE_URI = 'postgresql://flashcard_vti0_user:Rr0R6GU1RqD7ozEE8B0XzmSDA5iRFMKO@dpg-cjljgk8cfp5c73a5u0og-a.oregon-postgres.render.com/flashcard_vti0'
# os.environ.get('DATABASE_URL')
# postgresql://postgres:professor9@localhost:5432/flashcard
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.urandom(64)
