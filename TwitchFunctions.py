""" contains integration code for Twitch 
as well as functions that return Twitch data """

from flask import request
import requests
import json

#Integration information
CLIENT_ID = "5hi6d1chqez0e845sfgqrec0ls2e0n"
REDIRECT_URI = "http://127.0.0.1:5000/authorize"
CLIENT_SECRET = "0c72sjv7abz46vaouzw1a8w13k9q2j"

baseURL = "https://api.twitch.tv/kraken/"
authURL = baseURL+"oauth2/"
requestedScope = "viewing_activity_read user_subscriptions user_read channel_subscriptions"

def loginRequest():
    twitchLoginRequest = requests.get(authURL+"authorize?"+
    'client_id='+CLIENT_ID+
    '&redirect_uri='+REDIRECT_URI+
    '&response_type=code'+
    '&scope='+requestedScope)

    return twitchLoginRequest