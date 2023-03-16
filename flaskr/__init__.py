import sys
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from models import setup_db, ReactQuestion
from werkzeug.exceptions import HTTPException
from sqlalchemy.sql import func

def make_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS')
        return response

    @app.route('/')
    def index():
        return 'It works!'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/api/questions', methods = ['POST'])
    def create_question():
        question = request.json['question'].strip()
        optionA = request.json['optionA'].strip()
        optionB = request.json['optionB'].strip()
        optionC = request.json['optionC'].strip()
        optionD = request.json['optionD'].strip()
        answer = request.json['answer'].strip()

        error = False

        try:
            new_reactquestion = ReactQuestion(
                question,
                optionA,
                optionB,
                optionC,
                optionD,
                answer
            )
            new_reactquestion.insert()

            questions = ReactQuestion.query.order_by(ReactQuestion.id).all()
            format_questions = [question.serialize() for question in questions]
        
            return jsonify({
                'success': True,
                'created': new_reactquestion.id,
                'questions': format_questions,
                'total_questions': len(questions)
            }),200

        except:
            new_reactquestion.rollback_conn()
            error = True
            print(sys.exc_info())
        finally:
            new_reactquestion.close_conn()
        if error:
            abort(422)

    @app.route('/api/questions', methods = ['GET'])
    def get_question():
        try:
            questions = ReactQuestion.query.order_by(func.random()).all()
            format_questions = [question.serialize() for question in questions]

            return jsonify({
                'success': True,
                'questions': format_questions,
                'total_questions': len(questions)
            })
        except Exception as e:
            return(str(e))
    

    # CONVERT ABORT ERROR FROM HTML TO JSON
    @app.errorhandler(401)
    def not_found(error):
        return jsonify({
            "success": False, 
            "status": 401,
            "message": "Unauthorized",
        }), 401

    @app.errorhandler(403)
    def not_allowed(error):
        return jsonify({
            "success": False, 
            "status": 403,
            "message": "Method not allowed",
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, 
            "status": 404,
            "message": "API endpoint not found",
        }), 404
    
    @app.errorhandler(422)
    def not_processable(error):
        return jsonify({
            "success": False, 
            "status": 422,
            "message": "Unprocessable Entity",
        }), 422

    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            return e

        return jsonify({
            "success": False, 
            "status": 500,
            "message": " Internal Server Error",
            e:e
        }), 500

    return app