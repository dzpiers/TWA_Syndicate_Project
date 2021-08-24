import getTrackData
import getLyrics
import pandas as pd

def getPlayistData(song_ids):
    PlaylistData = []
    for id in song_ids:
        track_info = getTrackData.getTrackData(id)
        lyrics = getLyrics.getLyrics(track_info['artist'], track_info['name'])
        if lyrics != None:
            track_info['lyrics'] = lyrics
            PlaylistData.append(track_info)
    return PlaylistData

def getPlaylistCSV(playlist_data, csv_name):
    df = pd.DataFrame(playlist_data)
    df.to_csv(csv_name)