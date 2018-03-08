""" contains integration code for Twitch 
as well as functions that return Twitch data """

from flask import request
import requests
import json
import sys

#Integration information
CLIENT_ID = "5hi6d1chqez0e845sfgqrec0ls2e0n"
REDIRECT_URI = "http://127.0.0.1:5000/authorize"
CLIENT_SECRET = "0c72sjv7abz46vaouzw1a8w13k9q2j"


baseURL = "https://api.twitch.tv/kraken/"
authURL = baseURL+"oauth2/"
requestedScope = "viewing_activity_read user_subscriptions user_read channel_subscriptions"


#loginRequest function makes a get request to twitch
#which then returns a authorization token after login
def loginRequest():
    twitchLoginRequest = requests.get(authURL+"authorize?"+
    'client_id='+CLIENT_ID+
    '&redirect_uri='+REDIRECT_URI+
    '&response_type=code'+
    '&scope='+requestedScope)

    return twitchLoginRequest


#fetchAccessoken function posts to recieve an auth
#token from twitch, which then in stored
def fetchAccessToken():
    authCode = request.args.get('code')

    tokenRequest = requests.post(authURL+"/token?"+
    "client_id="+CLIENT_ID+
    "&client_secret="+CLIENT_SECRET+
    "&code="+authCode+
    "&grant_type=authorization_code"+
    "&redirect_uri="+REDIRECT_URI)

    tokenRequest = tokenRequest.json()

    #storing the access token
    #Could get the refresh token, scope list, and expiry
    #from the tokenRequest object

    #setting the local value of accessToken to global
    return tokenRequest.get('access_token')

def loadUserInfo(accessTkn):
    headers = {'Accept':'application/vnd.twitchtv.v5+json',
    'Client-ID': CLIENT_ID,
    'Authorization':'OAuth '+ accessTkn}

    userInfoRequest = requests.get('https://api.twitch.tv/kraken/user', headers = headers)
    userInfoRequest = userInfoRequest.json()

    userInfo = {}

    userInfo['userID'] = userInfoRequest.get('_id')
    userInfo['displayName'] = userInfoRequest.get('display_name')
    userInfo['picture'] = userInfoRequest.get('logo')
    userInfo['bio'] = userInfoRequest.get('bio')

    print(userInfo.get('displayName'), file=sys.stderr)

    #return copy of the dictionary full of the twitch user information
    return userInfo.copy()
    