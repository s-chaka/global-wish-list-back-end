from flask import Flask, request, jsonify, Response, Blueprint
from flask_pymongo import PyMongo, ObjectId
from app import db
from app import app
from user.models import User
# from bson import objectID

# Blueprint
# users_bp = Blueprint('users', __name__)
# @users_bp.route('/users', methods=['POST']) 


# helper function
def find_user(field,value ):
    users = db.users_collection
    output =[]
    for q in users.find({field:value}):
        output.append({'first_name': q['first_name'], 'last_name': q['last_name'],'email':q['email'],
                    'address':q['address'],'wish_list':q['wish_list'],'story':q['story']})
    if output:
        return jsonify({'result': output})
    else:
        return jsonify({'result': "No result found"})

# create user 
@app.route('/users', methods=['POST'])
def create_user():
    users = db.users_collection
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password =request.json['password']
    wish_list = request.json['wish_list']
    story = request.json['story']
    address = request.json['address']
    
    
    users_id = users.insert_one({'first_name': first_name, 'last_name': last_name, 'email': email,
        'password':password,'address':address, 'wish_list':wish_list, 'story': story}).inserted_id
    
    new_user = users.find_one({'_id': users_id})
    
    output = {'first_name': new_user['first_name'], 'last_name': new_user['last_name'], 'email': new_user['email'],
        'password':new_user['password'], 'address':new_user['address'], 'wish_list':new_user['wish_list'], 'story':new_user['story']}
    
    return jsonify({'result': 'user created successfully'})

#get all users information
@app.route('/users', methods=['GET'])
def get_all_users():
    users = db.users_collection
    output =[]
    for q in users.find():
        output.append({'first_name': q['first_name'], 'last_name': q['last_name'], 'email':q['email'],
                    'password':q['password'], 'address':q['address'], 'wish_list':q['wish_list'], 'story':q['story']})
    return jsonify({'result': output})

#get all users names
@app.route('/users/names', methods=['GET'])
def get_all_users_names():
    users = db.users_collection
    output =[]
    for q in users.find():
        output.append({'first_name': q['first_name'], 'last_name': q['last_name']})
    return jsonify({'result': output})


#get all users by country 
@app.route('/users/<country>', methods=['GET'])
def get_all_users_by_country(country):
    result = find_user('address.country', country)
    return result


# get one user by first name
@app.route('/users/fname/<first_name>', methods=['GET'])
def get_one_user_by_first_name(first_name):
    result = find_user('first_name', first_name)
    return result


# get one user by last name
@app.route('/users/lname/<last_name>', methods=['GET'])
def get_one_user_by_last_name(last_name):
    result = find_user('last_name', last_name)
    return result



# delete one user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    users = db.users_collection
    users.delete_one({'_id': ObjectId(id)})
    return jsonify({'result': 'user deleted  successfully'})

# update user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    users = db.users_collection
    _id = id
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password =request.json['password']
    address = request.json['address']
    wish_list = request.json['wish_list']
    story = request.json['story']
    
    if first_name and last_name and email and _id and password and address and request.method =='PUT':
        users.update_one({
            '_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'first_name': first_name, 
            'last_name': last_name, 'email':email, 'password': password, 'address': address, 'wish_list': wish_list, 'story':story
            }}
        )
        return jsonify({'result': 'user updated successfully'})
    else:
        return jsonify({'result': 'not found'})








    # users = db.users_collection
    # q = users.find_one({'first_name':first_name})
    # if q:
    #     output ={'first_name': q['first_name'], 'last_name': q['last_name'],'email':q['email'],
    #                 'address':q['address'], 'wish_list':q['wish_list'],'story':q['story']}
    # else:
    #     output = "No result found"
    # return jsonify({'result': output})





# @signup_bp.route('', methods=["POST"])
# def signup():
#     return User().signup()

# @signin_bp.route('/signin', methods=["GET"])
# def signin():
#     return User().signup()

# @signout_bp.route('/signout', methods=["GET"])
# def signin():
#     return User().signup()