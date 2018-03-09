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


#function that stores basic logged in user information into a dictionary
#storage of userid, displayname, picture CDN link, and bio
#returns the dictionary full of values mentioned in prev. comment
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

    #print(userInfo.get('displayName'), file=sys.stderr)

    #return copy of the dictionary full of the twitch user information
    return userInfo.copy()


def getTotals(userID_Param, headers_Param, req_url_param):

    #variable stores subscribers and followers
    #optionally holds either or both depending if they have followers or subscribers
    #example: totalsDict = {'followers':3}, 
        # totalsDict = {'subscribers':39}, 
        # totalsDict = {'followers':12, 'subscribers':99}
    totalsDict = {}

    #if no authorization, execute code to get channel followers count
    if headers_Param.get('Authorization') is None:
        #print("access token empty!"+ " UserID:"+str(userID_Param), file=sys.stderr)

        followers = requests.get(req_url_param, headers = headers_Param)

        followers = followers.json()

        if '_total' in followers.keys():
            totalsDict['followers'] = followers.get('_total')

            print(str(totalsDict), file=sys.stderr)



    #if there is an authorization in header, execute code to get channel subscriber count
    else:
        #accesstoken is parsed from the header for the print statement used in debugging below
        accessToken = headers_Param.get('Authorization')[6:]

        #print("Access Token: "+accessToken+ " UserID:"+str(userID_Param), file=sys.stderr)

        subscribers = requests.get(req_url_param, headers = headers_Param)

        subscribers = subscribers.json()

        if '_total' in subscribers.keys():
            totalsDict['subscribers'] = subscribers.get('_total')

            print(str(totalsDict), file=sys.stderr)

    #return the totalsDict
    #the totalsDict will have at one time subscribers, followers, or both
    return totalsDict

def getChannelFollowers(userID):
    headers = {'Accept':'application/vnd.twitchtv.v5+json',
    'Client-ID': CLIENT_ID}

    #replace hardcoded userID/channelID with real userid/channelID - 44322889
    requestUrl = baseURL+'channels/'+"44322889"+'/follows'

    getTotals(userID, headers, requestUrl)





    # followersList = []

    # for i in range(len(followObjectList)):
    #     followersList.append(followObjectList[i].get('user').get('display_name'))

    
def getChannelSubscribers(userID, accessToken):
    headers = {'Accept':'application/vnd.twitchtv.v5+json',
    'Client-ID': CLIENT_ID,
    'Authorization':'OAuth '+ accessToken }
    
    #replace hardcoded userID/channelID with real userid/channelID
    requestUrl = baseURL+'channels/'+'129454141'+'/subscriptions'

    getTotals(userID, headers, requestUrl)

