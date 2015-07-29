from flask import render_template, Blueprint, jsonify, url_for
from app import app
from config import config as cfg
import json
from flask import request, redirect
from app import db
from app.module_search import models as md

from app.module_search import models_es as mde


search = Blueprint('search', __name__)

@app.route('/')
@search.route('/')
@search.route('/index')
def index():
    return render_template('module_search/index.html', title='Home page', data={"base_url": request.url_root})

# @search.route('/users', methods=['POST'])
# def get_users():
#     """
#     Get People by name
#     ---
#     tags:
#         - search
#     parameters:
#         -   name: access_token
#             in: query
#             required: true
#             type: string
#             description: Access token of user
#         -   name: user_name
#             in: query
#             required: true
#             type: string
#             description: Name of user
#     responses:
#         200:
#             description: Returns a list of users
#         401:
#             description: Unauthorized
#         400:
#             description: Bad Request
#         500:
#             description: Server Internal error
#     """
#     user_name = request.args.get("user_name")
#     users = mde.User()
#     result = users.search_by_name(user_name)
#     return jsonify({'error_code': 0, "data": result})


# @search.route('/outfits/name', methods=['POST'])
# def get_outfits_by_name():
#     """
#     Get Outfit by name
#     ---
#     tags:
#         - search
#     parameters:
#         -   name: access_token
#             in: query
#             required: true
#             type: string
#             description: Access token of user
#         -   name: outfit_name
#             in: query
#             required: true
#             type: string
#             description: Name of outfit
#     responses:
#         200:
#             description: Returns a list of Outfits
#         401:
#             description: Unauthorized
#         400:
#             description: Bad Request
#         500:
#             description: Server Internal error
#     """
#     outfit_name = request.args.get("outfit_name")
#     outfits = mde.Outfit()
#     result = outfits.search_by_name(outfit_name)
#     return jsonify({'error_code': 0, "data": result})


# @search.route('/insert', methods=["POST"])
# def insert_user():
#     params = request.form
#     user = User(username=params['username'], password=params['password'], email=params['email'], first_name=params['first_name'], last_name=params['last_name'])
#     try:
#         db.session.add(user)
#         db.session.commit()

#         new_user = User.query.order_by(User.id.desc()).first()
#         es.index(index="test_feeder", doc_type="test_feeder_type", body={
#                     "id": new_user.id,\
#                     "username": new_user.username,\
#                     "password": new_user.password,\
#                     "first_name": new_user.first_name,\
#                     "last_name": new_user.last_name,\
#                     "email": new_user.email,\
#                 })
#     except Exception as e:
#         print(e)
#     return redirect(url_for("search.index"))

# @search.route("/delete/<int:id>")
# def delete_user(id):
#     try:
#         User.query.filter(User.id==id).delete()
#         db.session.commit()
#         es.delete_by_query(index='test_feeder', doc_type='test_feeder_type', body={
#                               "query": {
#                                            "match": {"id": id}
#                                        }
#                           })
#     except Exception as e:
#         print(e)
#     return redirect("/")

# @search.route("/get_user_by_name", methods=["POST"])
# def get_user_by_name():
#     params = request.data
#     #print(params)
#     username = params
#     print(username)
#     users = User.query.filter(User.username==username).all()
#     results = []
#     for u in users:
#         dicts = {
#             "id" : u.id,
#             "username": u.username,
#             "email": u.email,
#             "password": u.password,
#             "first_name": u.first_name,
#             "last_name": u.last_name
#         }
#         results.append(dicts)
#     data = json.dumps(results)
#     return data

