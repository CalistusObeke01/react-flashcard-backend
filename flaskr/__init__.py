from flask import Flask

def make_app(test_config=None):
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/greeting')
    def hi():
        return 'Hauwa, how far na?'

    return app