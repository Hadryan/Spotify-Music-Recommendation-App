import requests
from pprint import pprint

clientId = ''
clientSecret = ''
redirectUri = ''
accessToken = ''


def pullUserInfo(accessToken):

    baseUrl = 'https://api.spotify.com/v1/'
    headers = {'Authorization': 'Bearer {token}'.format(token=accessToken)}

    userInfo = requests.get(baseUrl + 'me', headers=headers)

    userPlaylists = requests.get(
        baseUrl +
        'users/{user_id}/playlists'.format(user_id=userInfo.json()['id']),
        headers=headers)

    userSavedSongs = requests.get(baseUrl + 'me/tracks', headers=headers)


pullUserInfo(accessToken)