from flask import Flask, redirect
import TwitchFunctions
import sys

accessToken = ""

#keys: userID, displayName, picture (cdn url), and bio
userInfoDict = {} 

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def loginPage():
    return redirect(TwitchFunctions.loginRequest().url)


@app.route('/authorize', methods = ['GET','POST'])
def getAuthorization():
    global accessToken

    accessToken = TwitchFunctions.fetchAccessToken()
    
    return redirect('/homepage')

@app.route('/homepage', methods = ['GET'])
def homepage():

    global userInfoDict

    userInfoDict =  TwitchFunctions.loadUserInfo(accessToken)

    TwitchFunctions.getChannelFollowers(userInfoDict.get('userID'))
    TwitchFunctions.getChannelSubscribers(accessToken)

    return "hi"
