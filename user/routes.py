from flask import Flask, request, jsonify, Response, Blueprint
from flask_pymongo import PyMongo #ObjectId
from app import db
from app import app
from user.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
# Blueprint
# users_bp = Blueprint('users', __name__)
# @users_bp.route('/users', methods=['POST']) 


# helper function
def find_user(field,value ):
    users = db.users_collection
    output =[]
    for q in users.find({field:value}):
        output.append({'first_name': q['first_name'], 'last_name': q['last_name'],'email':q['email'],
                    'address':q['address']})
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
    address = request.json['address']
    
    if first_name and last_name and email and password:
        hashed_password = generate_password_hash(password)
        id = users.insert_one({'first_name': first_name, 'last_name': last_name, 'email': email,
            'password':hashed_password,'address':address}).inserted_id
        print(str(ObjectId(id)))
    
    return jsonify({'result': 'user created successfully'})

#get all users information
@app.route('/users', methods=['GET'])
def get_all_users():
    users = db.users_collection
    output =[]
    for q in users.find():
        output.append({'_id':str(ObjectId(q['_id'])),'first_name': q['first_name'], 'last_name': q['last_name'], 'email':q['email'],
                    'password':q['password'], 'address':q['address']})
    return jsonify({'result': output})

#get all users names
@app.route('/users/names', methods=['GET'])
def get_all_users_names():
    users = db.users_collection
    output =[]
    for q in users.find():
        output.append({'first_name': q['first_name'], 'last_name': q['last_name']})
    return jsonify({'result': output})


#get user by id not working
@app.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    _id =str(ObjectId(user_id))
    users = db.users_collection
    output =[]
    print(_id)
    for q in users.find({'user_id':_id}):
        output.append({'user_id':q['user_id'],'first_name': q['first_name'], 'last_name': q['last_name']})
    return jsonify({'result': output})


#get users by country 
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

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password =request.json['password']
    address = request.json['address']
    
    if first_name and last_name and email and password and address:
        hashed_password = generate_password_hash(password)
        users.update_one({'_id': ObjectId(id)}, {'$set': {'first_name': first_name, 
            'last_name': last_name, 'email':email, 'password': hashed_password, 'address': address }}
        )
        return jsonify({'result': 'user updated successfully'})
    else:
        return jsonify({'result': 'not found'})
    
#********************************** WISH ********************************************#

# create wish for specific user 

@app.route('/users/<user_id>/wishlist', methods=['POST'])
def create_wish_for_user(user_id):
    _id = ObjectId(user_id)
    owner_id = str(_id)
    
    wishes = db.wish_list_collection
    
    wish = request.json['wish']
    story = request.json['story']
    
    if wish and story:
        wishes.insert_one({'wish': wish, 'story': story, 'owner_id':owner_id})
        
    # wish_id = wishes.insert_one({'wish': wish_list, 'story': story, 'owner_id':owner_id}).inserted_id
    # new_wish = wishes.find_one({'_id': wish_id})
    # output = {'wish': new_wish['wish'], 'story': new_wish['story'], 'owner_id':new_wish['owner_id']}

    return jsonify({'result': 'wish created successfully'}) 

# get specific user wish
@app.route('/users/<user_id>/wishlist', methods=['GET'])
def get_users_wish_by_id(user_id):
    _id = ObjectId(user_id)
    wishes = db.wish_list_collection
    
    output =[]
    for q in wishes.find({'owner_id':user_id}):
        output.append({ 'wish':q['wish'], 'story':q['story']})
    return jsonify({'result': output})

# it's working
@app.route("/users/wishes", methods=['GET'])
def get_users_wish():
    # _id = ObjectId(user_id)
    wishes = db.wish_list_collection
    
    output =[]
    for q in wishes.find():
        output.append({ '_id':str(ObjectId(q['_id'])),'owner_id':q['owner_id'],'wish':q['wish'], 'story':q['story']})
    return jsonify({'result': output})

# update wishes
@app.route('/users/<user_id>/wishlist', methods=['PUT'])
def update_users_wish(user_id):
    _id = ObjectId(user_id)
    wishes = db.wish_list_collection
    
    wish = request.json['wish']
    story = request.json['story']
    
    if wish and story:
        wishes.update_one({'_id':ObjectId(user_id)},{'$set':{'wish':wish, 
                        'story':story}})
        return jsonify({'result': 'wish updated successfully'})
    else:
        return jsonify({'result': 'not found'})    
    
#delete wish
@app.route('/users/<wish_id>/wishlist', methods=['DELETE'])
def delete_users_wish(wish_id):
    wishes = db.wish_list_collection
    wishes.delete_one({'_id': ObjectId(wish_id)})
    return jsonify({'result': 'wish deleted  successfully'})