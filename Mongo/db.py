from flask import Flask, request
from pymongo import MongoClient

app = Flask('__main__')
client = MongoClient('127.0.0.1',27017)

db_name = "WebApp"
webapp = client[db_name]

collection_name = "Users"
collection = webapp[collection_name]

@app.route("/")
def home():
    return "Users DB"

# Create
@app.route("/adduser/<user>",methods=["POST"])
def createUser(user):
    print(user)
    collection.insert_one({"name":user})
    return "User Added"

# Read
@app.route("/list",methods = ["GET"])
def listUsers():
    listOfUsers = []
    for i in collection.find():
        listOfUsers.append(i)
    return str(listOfUsers)

# Update
def updateUser(user):
    collection.update_one(user)
    return "User Updated"

# Delete
def deleteUser(user):
    collection.delete_one(user)
    return "User Deleted"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)