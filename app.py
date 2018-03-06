from flask import Flask, redirect

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def loginPage():
    return "test login page"


@app.route('/authorize', methods = ['GET','POST'])
def getAuthorization():
    return "test authorize"

@app.route('/homepage', methods = ['GET'])
def homepage():
    return "test homepage"
