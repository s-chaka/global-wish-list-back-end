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
connection_string = f'mongodb+srv://sdatabase:{password}@mydb.6b0j3ai.mongodb.net/?retryWrites=false&w=majority'
client = MongoClient(connection_string)

db = client.global_wish_list
users = db.users_collection


if __name__ == '__main__':
    app.run(debug=True)



from user import routes



# Register Blueprints 
# from user.routes import users_bp
# app.register_blueprint(users_bp)















# def insert_test_doc():
#     collection = users
#     test_document = {
#         'name': "selam",
#         'owner': "yes"        
#     }
#     inserted_id = collection.insert_one(test_document).inserted_id
#     print(inserted_id)
# insert_test_doc()




    # name = request.json['name']
    # owner = request.json['owner']
    
    # users_id = users.insert_one({'name': name, 'owner': owner}).inserted_id
    # new_user = users.find_one({'_id': users_id})
    # users_id = users.insert_one({'name': name, 'owner': owner}).inserted_id
    # new_user = users.find_one({'_id': users_id})
    
    # output = {'name': new_user['name'], 'owner': new_user['owner']}
    
    # return jsonify({'result': output})





# @app.route("/")
# def home():
#     return "Home"

# @app.route("/profile/")
# def profile():
#     return "Profile"




# clinet = pymongo.MongoClient(host='localhost', port=27017)
# db = clinet.company


# @app.route("/users",methods=["POST"])
# def create_user():
#     user = {'name': 'selam', 'lastName':'chaka'}
#     dbResponse = db.users.insert_one(user)
    # return user
    # try:
    #     user = {'name': 'selam', 'lastName':'chaka'}
    #     dbResponse = db.users.insert_one(user)
    #     for attr in dir(dbResponse):
    #         print(attr)
        # print(dbResponse.inserted_id)
        # return Response(
        #     response = {"message":"user created", 'id':f"{dbResponse.inserted_id}"},
        #     status = 200,
        #     mimetype="application/json"
        # )
        
    # except Exception as ex:
    #     print('*************')
    #     print(ex)
    #     print('*************')

# if __name__== "__main__":
#     app.run(port=5555, debug=True)



# dbs = client.list_database_names()
# test_db = client.test
# collections = test_db.list_collection_names()
# print(collections)

# def insert_test_doc():
#     collection = test_db.test 
#     test_document = {
#         'name': "selam",
#         'owner': "yes"        
#     }
#     inserted_id = collection.insert_one(test_document).inserted_id
#     print(inserted_id)
# insert_test_doc()

# global_wish_list = client.global_wish_list
# users_collection = global_wish_list.users_collection

# def create_users_documents():
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
#     docs = []
#     for first_name, last_name, email, password,address in zip(first_names,last_names,eimals,passwords,addresses):
#         doc = {'first_name':first_name,'last_name':last_name,'email': email,'password':password, 'address':address}
#         print(doc)
#         docs.append(doc)
#     users_collection.insert_many(docs)
# create_users_documents()






# from flask_cors import CORS



# from user import routes 



# @app.route('/')
# def home():
#     return "Home"
    

# app.config['MONGO_URI']='mongodb://localhost/global_wish_list_development'
# mongo = PyMongo(app)

# CORS(app)

# db = mongo.db.users

# # @app.route('/')
# # def index():
# #     return '<h1> Hello world</h1>'

# @app.route('/users', methods=['POST'])
# def createAccount():
#     id = db.insert({
#         'first name':request.json['first name'],
#         'last name':request.json['last name'],
#         'eimal':request.json['email'],
#         'country':request.json['country'],
#         'city name':request.json['city name'],
#         'street address':request.json['stree address']
#         'password':request.json['password']
#     })
#     return jsonify({'user': str()})

