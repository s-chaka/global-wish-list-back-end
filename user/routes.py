from flask import Flask, request, jsonify, Response, Blueprint
from flask_pymongo import PyMongo, ObjectId
from app import db
from user.models import User
# from bson import objectID


# Blueprints
signup_bp = Blueprint('signup', __name__, url_prefix="/signup")
signin_bp = Blueprint('signin', __name__, url_prefix="/signin")
signout_bp = Blueprint('signout', __name__, url_prefix="/signout")

@signup_bp.route('', methods=['POST'])
def createAccount():
    id = db.insert({
        'first_name'.request.json['first_name'],
        'last_name'.request.json['last_name'],
        'email'.request.json['email'],
        'password'.request.json['password'],
        'address'.request.json['address'],
    
    })
    return jsonify({'id': str(ObjectId(id)), 'message':"user created succesfully"})

#     first_names= ['Tomas', 'Sara', 'Jose', 'Brad', 'Allen']
#     last_names= ['Smith', 'Bart', 'Pit', 'Cater', 'Geral']
#     eimals = ['tomas@gmail.com','sara@gmail.com','jose@gmail.com','brad@gmail.com','allen@gmail.com']
#     passwords= ['password1','password2','password3','password4','password5']
#     addresses = [ 
#             {'country':'USA', 'city_name': 'new york', 'street_address': '1234 main street'},
#             {'country':'Uganda', 'city_name': 'new city', 'street_address': '8888 main street'},
#             {'country':'Canada', 'city_name': 'another city', 'street_address': '9999 main street'},
#             {'country':'USA', 'city_name': 'city', 'street_address': '1212 main street'},
#             {'country': 'South Africa','city_name': 'city', 'street_address': '5151 main street'}
#             ]

# @signup_bp.route('', methods=["POST"])
# def signup():
#     return User().signup()

# @signin_bp.route('/signin', methods=["GET"])
# def signin():
#     return User().signup()

# @signout_bp.route('/signout', methods=["GET"])
# def signin():
#     return User().signup()