from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()
genius_key = os.getenv("GENIUS_KEY")

def getGeniusURL(track_artist, track_name, genius_key=genius_key):
    try:
        base_url = 'https://api.genius.com'
        headers = {'Authorization': 'Bearer ' + genius_key}
        search_url = base_url + '/search'
        data = {'q': track_name + ' ' + track_artist}
        response = requests.get(search_url, data=data, headers=headers)
        json = response.json()
        remote_song_info = None
        for hit in json['response']['hits']:
            if track_artist.lower() in hit['result']['primary_artist']['name'].lower():
                remote_song_info = hit
                break
        genius_url = remote_song_info['result']['url']
        return genius_url
    except:
        return None

def getLyrics(genius_url):
    try:
        if genius_url != None:
            page = requests.get(genius_url)
            html = BeautifulSoup(page.text, 'html.parser')
            lyrics1 = html.find("div", class_="lyrics")
            lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
            if lyrics1:
                lyrics = lyrics1.get_text()
            elif lyrics2:
                lyrics = lyrics2.get_text()
            elif lyrics1 == lyrics2 == None:
                lyrics = None
            if len(lyrics) < 10000:
                return lyrics
        else:
            return None
    except:
        return None

'Help from https://towardsdatascience.com/become-a-lyrical-genius-4362e7710e43'