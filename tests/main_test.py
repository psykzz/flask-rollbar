from flask_rollbar import Rollbar
import unittest


def create_test_app():
    import os
    from flask import Flask
    app = Flask(__name__)
    app.config.update({
        'ROLLBAR_ENABLED': True,
        'ROLLBAR_SERVER_KEY': os.environ.get('ROLLBAR_API_KEY'),
    })
    Rollbar(app)

    @app.route('/')
    def home():
        test = [1, 2, 3]
        test[3]
        return "hello"

    return app


class FlaskRollbarTestCase(unittest.TestCase):

    def setUp(self):
        test_app = create_test_app()
        test_app.config['TESTING'] = True
        self.app = test_app.test_client()

    def test_error(self):
        self.app.get('/')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
