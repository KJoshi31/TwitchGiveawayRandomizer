#This file has helpful twitch functions
import json
import requests

url = 'https://api.twitch.tv/helix/users?login='

#returns the login name, id, and display name of a user
#within a list of user information
def getLoginNameAndIDAndDisplayName(userData):
    json_data = json.loads(userData.text)
    userInfoDictionary = json_data['data'][0]
    #print(userInfoDictionary)

    userID = {'id':userInfoDictionary.get('id')}
    login = {'login':userInfoDictionary.get('login')}
    displayName = {'displayName':userInfoDictionary.get('display_name')}

    userInfoList = [userID,login,displayName]

    return userInfoList
    