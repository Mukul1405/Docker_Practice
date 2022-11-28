from flask import Flask
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os
# import sys

# os.environ['MONGODB_USERNAME'] = sys.argv[1]
# os.environ['MONGODB_PASSWORD'] = sys.argv[2]
# os.environ['MONGODB_HOSTNAME'] = sys.argv[3]
# os.environ['MONGODB_DATABASE'] = sys.argv[4]

print(os.environ['MONGODB_USERNAME'],
os.environ['MONGODB_PASSWORD'],
os.environ['MONGODB_HOSTNAME'],
os.environ['MONGODB_DATABASE']
)

app = Flask('__main__')
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

# db_name = "WebApp"
# webapp = client['db_name']

# collection_name = "Users"
# collection = webapp['collection_name']
mongo = PyMongo(app)
collection = mongo.db

@app.route("/")
def home():
    return "Users DB"

# Create
@app.route("/adduser/<user>",methods=["POST"])
def createUser(user):
    print(user)
    collection.users.insert_one({"name":user})
    return "User Added"

# Read
@app.route("/list",methods = ["GET"])
def listUsers():
    listOfUsers = []
    for i in collection.users.find():
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