from flask import Flask,request
from pymongo import MongoClient
import requests
import os

app = Flask('__main__')
# app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
client = MongoClient('mongodb://'+ os.environ['username'] + ":" + os.environ['password'] + '@mongodb:27017/WebApp')
# client.WebApp.authenticate(os.environ['username'], os.environ['password'], mechanism='MONGODB-CR')

db = client.WebApp #db 
user_collection = db.User  #collection


@app.route("/")
def home():
    resp = requests.get("http://mongodb:27017")
    return f"Connection with mongodb container - {resp.text}"

# Create
@app.route("/adduser/<user>",methods=["POST"])
def createUser(user):
    print(user)
    user_collection.insert_one({"name":user})
    return "User Added"

# Read
@app.route("/list",methods = ["GET"])
def listUsers():
    listOfUsers = []
    for i in user_collection.find():
        listOfUsers.append(i)
    if len(listOfUsers) is not 0:
        return str(listOfUsers)
    return "No Users in DB Right now"

# # Update
# def updateUser(user):
#     collection.update_one(user) 
#     return "User Updated"

# # Delete
# def deleteUser(user):
#     collection.delete_one(user)
#     return "User Deleted"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)