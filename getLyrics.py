import lyricsgenius
from dotenv import load_dotenv
import os

load_dotenv()
genius_token = os.getenv("GENIUS_TOKEN")

'Insert your own Genius authorization token here'

genius = lyricsgenius.Genius(genius_token)

def getLyrics(artistname, songname):
    try:
        song = genius.search_artist(artistname, max_songs=0, include_features=True).song(songname)
        lyrics = song.lyrics
        if len(lyrics) <= 10000:
            return lyrics
        return None
    except:
        return None

'Help from https://github.com/johnwmillr/LyricsGenius/blob/master/README.md'