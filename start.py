import requests
import json
from pprint import pprint

clientId = ''
clientSecret = ''
redirectUri = ''

accessToken = ''
baseUrl = 'https://api.spotify.com/v1/'
headers = {'Authorization': 'Bearer {token}'.format(token=accessToken)}


def getUserInfo():
    # Get User Info
    userInfo = requests.get(baseUrl + 'me', headers=headers)

    # Get User's Saved Songs
    userSavedSongs = requests.get(baseUrl + 'me/tracks?limit=5',
                                  headers=headers).json()

    # Print information on each saved song
    for song in userSavedSongs['items']:
        artistName = song['track']['album']['artists'][0]['name']
        songName = song['track']['name']

        print("Artist : %s, Song : %s" % (artistName, songName))


def getUsersTopArtists():
    usersTopArtists = requests.get(baseUrl + 'me/top/artists?limit=5',
                                   headers=headers).json()

    # Print information on each top artist
    for artist in usersTopArtists['items']:
        artistName = artist['name']
        print("Artist Name : %s" % artistName)


def getUsersTopTracks():
    usersTopTracks = requests.get(baseUrl + 'me/top/tracks?limit=5',
                                  headers=headers).json()

    # Print information on each top artist
    for track in usersTopTracks['items']:
        songName = track['name']
        print("Song Name : %s" % songName)


getUsersTopArtists()
getUsersTopTracks()
