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
    '''
    keys = playlist_data[0].keys()
    with open(csv_name, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        for row in playlist_data:
            try:
                dict_writer.writerow(row)
            except:
                pass


for id in song_ids:
    track_info = track_data.getTrackData(id)
    lyrics = genius.getLyrics(track_info['artist'], track_info['name'])
    track_info['lyrics'] = lyrics
    print(track_info)
'''