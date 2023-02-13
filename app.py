from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from pymongo import MongoClient
from flask_pymongo import PyMongo ,ObjectId
# import pymongo
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



app = Flask(__name__)
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

password = os.environ.get("MONGODB_PWD")
connection_string = f'mongodb+srv://sdatabase:{password}@mydb.6b0j3ai.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connection_string)

db = client.global_wish_list
users = db.users_collection


if __name__ == '__main__':
    app.run(debug=True)



from user import routes
