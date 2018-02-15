#Twitch client ID information
import requests
import TwitchFunctions
import json

#Client ID for this application
headers = {'Client-ID' :'5hi6d1chqez0e845sfgqrec0ls2e0n'}
url = 'https://api.twitch.tv/helix/'

#list will be populated with id, login, display name dictionaries
userInformationList = []

#get basic user information
#must be initialized first to use rest of classes
def getBasicUserInformation(username):
    username = username.lower().strip()
    #'https://api.twitch.tv/helix/users?login=ronmoz'
    usernameGetResponse = requests.get(url+'/users?login='+username, headers=headers)
    
    #print(usernameGetResponse.text)
    
    global userInformationList

    userInformationList =  TwitchFunctions.getLoginNameAndIDAndDisplayName(usernameGetResponse)

def getFollowers():

    if len(userInformationList) == 0:
        print("Must call the getBasicUserInformation function first\nExiting")
        return

    followersGetResponse = requests.get(url+'/users/follows?to_id='+userInformationList[0]['id'], headers=headers)

    print(followersGetResponse.text)



getBasicUserInformation('ronmoz')
getFollowers()
