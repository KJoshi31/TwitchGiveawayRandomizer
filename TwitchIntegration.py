import requests


headers = {'Client-ID' :'5hi6d1chqez0e845sfgqrec0ls2e0n'}
url = 'https://api.twitch.tv/helix/users?login=ronmoz'
r = requests.get(url, headers=headers)

print(r.text)