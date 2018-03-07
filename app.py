from flask import Flask, redirect
import TwitchFunctions

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def loginPage():
    twitchLoginRequest = TwitchFunctions.loginRequest()
    return redirect(twitchLoginRequest.url)


@app.route('/authorize', methods = ['GET','POST'])
def getAuthorization():
    return "test authorize"

@app.route('/homepage', methods = ['GET'])
def homepage():
    return "test homepage"
