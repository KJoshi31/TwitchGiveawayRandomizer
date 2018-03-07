from flask import Flask, redirect
import TwitchFunctions

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def loginPage():
    return redirect(TwitchFunctions.loginRequest().url)


@app.route('/authorize', methods = ['GET','POST'])
def getAuthorization():
    TwitchFunctions.fetchAccessToken()
    return redirect('/homepage')

@app.route('/homepage', methods = ['GET'])
def homepage():
    return "test homepage"
