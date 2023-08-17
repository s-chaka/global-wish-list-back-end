from flask import Flask, request, jsonify, Response, make_response, Blueprint
from flask_pymongo import PyMongo 
from app import db
from app import app
# from user.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
from bson.objectid import ObjectId
from bson import json_util
from flask import json



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

#get all users 
@app.route('/users', methods=['GET'])
def get_all_users():
    users = db.users_collection
    output =[]
    for q in users.find():
        output.append({'_id':str(ObjectId(q['_id'])),'first_name': q['first_name'], 'last_name': q['last_name'], 'email':q['email'],
                    'password':q['password'], 'address':q['address']})
    return jsonify({'result': output})

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
        # hashed_password = generate_password_hash(password)
        id = users.insert_one({'first_name': first_name, 'last_name': last_name, 'email': email,
            'password':password,'address':address}).inserted_id
        # idd=(str(ObjectId(id)))
    
    new_user = users.find_one({'_id': id})

    output = {'first_name': new_user['first_name'], 'last_name': new_user['last_name'], 'email':new_user['email'],
            'password':new_user['password'],'address':new_user['address']}

    return Response(json.dumps(new_user,default=str),mimetype="application/json")


#get all users names
@app.route('/users/names', methods=['GET'])
def get_all_users_names():
    users = db.users_collection
    output =[]
    for q in users.find():
        output.append({'first_name': q['first_name'], 'last_name': q['last_name']})
    return jsonify({'result': output})


#get user by id not working
@app.route('/users/<string:id>', methods=['GET'])
def get_user_by_id(id):
    data = db.users_collection.find_one({'_id':ObjectId(id)})
    id = data['_id']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address= data['address']
    dataDict={
        'id':str(id),
        'first_name':first_name,
        'last_name': last_name,
        'email': email,
        'address': address
    }
    return jsonify(dataDict)

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



# delete user
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
        # hashed_password = generate_password_hash(password)
        users.update_one({'_id': ObjectId(id)}, {'$set': {'first_name': first_name, 
            'last_name': last_name, 'email':email, 'password': password, 'address': address }}
        )
        return jsonify({'result': 'user updated successfully'})
    else:
        return jsonify({'result': 'not found'})
    
#********************************** WISH ********************************************#

# create wish by user id 

@app.route('/users/<user_id>/wishlist', methods=['POST'])
def create_wish_for_user(user_id):
    _id = ObjectId(user_id)
    owner_id = str(_id) 
    wishes = db.wish_list_collection
    url = request.json['url']
    wish = request.json['wish']
    story = request.json['story']
    interested = False
    satisfied = False
    
    if wish and story:
        wishes.insert_one({'url':url,'wish': wish, 'story': story, 'owner_id':owner_id, 'interested':interested, 'satisfied':satisfied})
        
    return jsonify({'result': 'wish created successfully'}) 

# get user wish by id
@app.route('/users/<user_id>/wishlist', methods=['GET'])
def get_users_wish_by_id(user_id):
    _id = ObjectId(user_id)
    wishes = db.wish_list_collection
    
    output =[]
    for q in wishes.find({'owner_id':user_id}):
        output.append({'url':q['url'], 'wish':q['wish'], 'story':q['story'], 'interested':q['interested'],
                    'satisfied':q['satisfied'] })
    return jsonify({'result': output})

# Get users wish
@app.route("/users/wishes", methods=['GET'])
def get_users_wish():

    wishes = db.wish_list_collection
    
    output =[]
    for q in wishes.find():
        output.append({ '_id':str(ObjectId(q['_id'])),'owner_id':q['owner_id'],'url':q['url'],'wish':q['wish'], 'story':q['story'],'interested':q['interested'],'satisfied':q['satisfied']})
    return jsonify({'result': output})

# update wishes
@app.route('/users/<wish_id>/wishlist', methods=['PUT'])
def update_users_wish(wish_id):
    _id = ObjectId(wish_id)
    wishes = db.wish_list_collection
    wish = request.json['wish']
    story = request.json['story']
    interested = request.json["interested"]
    satisfied = request.json["satisfied"]
    
    if wish and story:
        wishes.update_one({'_id':ObjectId(wish_id)},{'$set':{'wish':wish, 
                        'story':story, 'interested':interested,'satisfied':satisfied}})
        return jsonify({'result': 'wish updated successfully'})
    else:
        return jsonify({'result': 'not found'})    
    
#delete wish
@app.route('/users/<wish_id>/wishlist', methods=['DELETE'])
def delete_users_wish(wish_id):
    wishes = db.wish_list_collection
    wishes.delete_one({'_id': ObjectId(wish_id)})
    return jsonify({'result': 'wish deleted  successfully'})