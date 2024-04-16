from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from pymongo import MongoClient
from flask_pymongo import PyMongo ,ObjectId
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



app = Flask(__name__)
bcrypt = Bcrypt(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

password = os.environ.get("MONGODB_PWD")
connection_string = f'mongodb+srv://sdatabase:{password}@mydb.6b0j3ai.mongodb.net/'
client = MongoClient(connection_string)

db = client.global_wish_list
users = db.users_collection

from user.routes import app as user_app
app.register_blueprint(user_app)

if __name__ == '__main__':
    app.run(debug=True)



