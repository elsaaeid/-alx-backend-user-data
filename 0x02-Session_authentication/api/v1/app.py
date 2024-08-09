#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = os.getenv('AUTH_TYPE')
if auth:
    if auth == 'basic_auth':
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()
    elif auth == 'session_auth':
        from api.v1.auth.session_auth import SessionAuth
        auth = SessionAuth()
    elif auth == 'session_exp_auth':
        from api.v1.auth.session_exp_auth import SessionExpAuth
        auth = SessionExpAuth()
    elif auth == 'session_db_auth':
        from api.v1.auth.session_db_auth import SessionDBAuth
        auth = SessionDBAuth()
    else:
        from api.v1.auth.auth import Auth
        auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Unauthorized access handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def not_allowed(error) -> str:
    """
    Not allowed access handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def auth_filter():
    """
    Filtering each request for
    authentication purposes
    """
    # If auth is None, do nothing
    if auth is None:
        return
    # Create list of excluded paths
    exclude_list = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']
    # if request.path is not part of the list above, do nothing
    # You must use the method require_auth from the auth instance
    if not auth.require_auth(request.path, exclude_list):
        return
    # If auth.authorization_header(request) and auth.session_cookie(request)
    # return None, raise the error, 401 - you must use abort
    auth_header = auth.authorization_header(request)
    session_cookie = auth.session_cookie(request)
    if auth_header is None and session_cookie is None:
        abort(401)
    # If auth.current_user(request) returns None, raise the error 403 - you
    # must use abort
    user = auth.current_user(request)
    if user is None:
        abort(403)
    # Assign the result of auth.current_user(request) to request.current_user
    request.current_user = user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
