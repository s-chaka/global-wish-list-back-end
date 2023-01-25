from flask import Flask, request, jsonify, Response
# from passlib.hash import pbkdf2_sha256
from app import db

class User:
    def signup(self):
        user = {
            "_id":"",
            "name":"",
            "email":"",
            "password":""
        }
        # encrypt the password
        # user["password"] = pbkdf2_sha256.encrypt(user['password'])
        
        db.users.insert_one(user)
        return jsonify(user), 200
    
    
    # def signin(self):
    #     user = {
    #         "_id":"",
    #         "email":"",
    #         "password":""
    #     }
    #     return jsonify(user), 200
    # def signout(self):
    #     user = {
    
    #     }
    #     return jsonify(user), 200
    
    
    
    
    
    
    
    
    

    # def __init__(self, username, first_name, last_name, email, _id, address):
    #     self.username = username
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self._id = _id
    #     self.address = address 