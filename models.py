from sqlalchemy import Column, String
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def setup_db(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

class ReactQuestion(db.Model):
    __tablename__ = 'reactquestions'

    id = db.Column(db.Integer, primary_key=True)
    question = Column(String, nullable=False)
    optionA = Column(String, nullable=False)
    optionB = Column(String, nullable=False)
    optionC = Column(String, nullable=False)
    optionD = Column(String, nullable=False)
    answer = Column(String, nullable=False)

    def __init__(self, question, optionA, optionB, optionC, optionD, answer):
        self.question= question
        self.optionA = optionA
        self.optionB = optionB
        self.optionC = optionC
        self.optionD = optionD
        self.answer = answer

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def close_conn(self):
        db.session.close()

    def rollback_conn(self):
        db.session.rollback()

    def serialize(self):
        return {
        'id': self.id,
        'question': self.question,
        'optionA': self.optionA,
        'optionB': self.optionB,
        'optionC': self.optionC,
        'optionD': self.optionD,
        'answer': self.answer
    }
