import lyricsgenius
from dotenv import load_dotenv
import os

load_dotenv()
genius_token = os.getenv("GENIUS_TOKEN")
genius = lyricsgenius.Genius(genius_token)

def getLyrics(artistname, songname):
    song = genius.search_artist(artistname, max_songs=0, include_features=True).song(songname)
    try:
        lyrics = song.lyrics
        if len(lyrics) <= 10000:
            return lyrics
        return None
    except:
        return None

'''
rules = getLyrics("Queen", "Bohemian Rhapsody")
print('=================')
print(rules)
'''

'https://github.com/johnwmillr/LyricsGenius/blob/master/README.md'