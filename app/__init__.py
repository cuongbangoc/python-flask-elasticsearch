from flask import Flask, jsonify, Blueprint, request, make_response
from flask.ext.sqlalchemy import SQLAlchemy
import jinja2
from config import config as cfg

from flask_swagger import swagger
import sys, http.client

app = Flask(__name__, template_folder=cfg.TEMPLATE_ROOT, static_folder=cfg.STATIC_ROOT)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(cfg.MYSQL_USER, cfg.MYSQL_PASSWORD, cfg.MYSQL_HOST, cfg.MYSQL_DB)
db = SQLAlchemy(app)

from app.common import elastic as es
es = es.Elastic()

# initial log application
if cfg.DEBUG:
    from logging import Formatter
    import logging
    file_handler = logging.FileHandler(cfg.LOG_FILE)
    if cfg.LOG_LEVEL not in [0, 10, 20, 30, 40, 50]:
        file_handler.setLevel(0)
    else:
        file_handler.setLevel(cfg.LOG_LEVEL)
    file_handler.setFormatter(Formatter(cfg.LOG_FORMAT))
    app.logger.addHandler(file_handler)

# initial a module
from app.module_search import controllers

# initial blueprint
app.register_blueprint(controllers.search, url_prefix='/search')

# Error Handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error_code': http.client.NOT_FOUND, 'message': 'Not Found'}), http.client.NOT_FOUND)

# Error Handler
@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error_code': http.client.INTERNAL_SERVER_ERROR, 'message': 'Not Found'}), http.client.INTERNAL_SERVER_ERROR)

# Swagger Doccument for API
@app.route('/docs')
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Search API"
    swag['basePath'] = "/"
    return jsonify(swag)

# Cross origin
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
    response.headers.add('Access-Control-Expose-Headers', "Authorization")
    response.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
    response.headers.add('Access-Control-Allow-Credentials', "true")
    response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
    return response
