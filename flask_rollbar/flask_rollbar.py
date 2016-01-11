import os
from rollbar import init, report_message, report_exc_info
import rollbar.contrib.flask

from flask import got_request_exception
from flask import Request as OriginalFlaskRequest


class FlaskRollbarException(Exception):
    pass


class RequestAlreadyModified(FlaskRollbarException):
    pass


class InvalidRollbarRequest(FlaskRollbarException):
    pass


class InvalidServerKey(FlaskRollbarException):
    pass


class Rollbar(object):
    '''
    Basic Rollbar Implementation
    '''
    def __init__(self, app=None, request_handler=None):
        self.custom_request_handler = request_handler
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        # Basic Configuration settings.
        self._enabled = bool(app.config.get(
            'ROLLBAR_ENABLED',
            os.environ.get('ROLLBAR_ENABLED', False)))

        self._server_key = app.config.get(
            'ROLLBAR_SERVER_KEY',
            os.environ.get('ROLLBAR_SERVER_KEY', False))

        self._environment = app.config.get(
            'ROLLBAR_ENVIRONMENT',
            'development')

        self._allow_new_request = app.config.get(
            'ROLLBAR_OVERWRITE_REQUEST',
            False)

        if self._enabled and not self._server_key:
            raise InvalidServerKey("Invalid Rollbar server key provided")

        @app.before_first_request
        def init_rollbar():

            if self._enabled:

                # Example taken from https://github.com/rollbar/rollbar-flask-example/blob/master/hello.py
                self._rb = init(
                    self._server_key,
                    self._environment,
                    root=os.path.dirname(os.path.realpath(__file__)),  # server root directory, makes tracebacks prettier
                    allow_logging_basic_config=False)  # flask already sets up logging

                got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

        if self.custom_request_handler is not None:
            if not self._allow_new_request and app.request_class is not OriginalFlaskRequest:
                raise RequestAlreadyModified("The original request was already modified by another system")

            if not hasattr(self.custom_request_handler, 'rollbar_person'):
                raise InvalidRollbarRequest("Custom request handler does not have a rollbar person property")
            app.request_class = self.custom_request_handler

    def report_message(self, message, level):
        return report_message(message, level)

    def report_exc_info(self):
        return report_exc_info()
