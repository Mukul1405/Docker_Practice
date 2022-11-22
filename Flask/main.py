from flask import Flask
import requests


app = Flask('__main__')

@app.route("/")
def home():
    return "Home Page"

@app.route("/users",methods = ["GET"])
def listUsers():
    resp = requests.get("0.0.0.0:5002/list")    
    return resp

@app.route("/adduser/<user>",methods = ["POST"])
def addUser():
    resp = requests.post("0.0.0.0:5002/adduser/user")
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)