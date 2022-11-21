from flask import Flask, request

app = Flask('__main__')

@app.route("/")
def home():
    return "Home Page"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)