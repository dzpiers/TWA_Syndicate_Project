import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def getTrackID(user, playlist_id):
    id = []
    play_list = sp.user_playlist(user, playlist_id)
    for item in play_list['tracks']['items']:
        track = item['track']
        id.append(track['id'])
    return id

def getTrackData(id):
    meta = sp.track(id)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    url = meta['external_urls']['spotify']

    track = {}
    track['name'] = name
    track['album'] = album
    track['artist'] = artist
    track['release date'] = release_date
    track['length'] = length
    track['popularity'] = popularity
    track['url'] = url

    return track

'''
id = getTrackID("dhruv.piers", "3odNjkuC77flx2Aob21Ejp")
for song in id:
    print(getTrackData(song))
'''

'https://morioh.com/p/31b8a607b2b0'