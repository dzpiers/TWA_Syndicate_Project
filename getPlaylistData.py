import getTrackData
import getLyrics
import pandas as pd

def getPlayistData(*argv):
    PlaylistData = []
    for playlist_no, arg in enumerate(argv):
        for track_no, id in enumerate(arg):
            track_info = getTrackData.getTrackData(id)
            genius_url = getLyrics.getGeniusURL(track_info['artist'], track_info['name'])
            lyrics = getLyrics.getLyrics(genius_url)
            if lyrics != None:
                track_info['lyrics'] = lyrics
                PlaylistData.append(track_info)
            else:
                lyrics = getLyrics.getLyrics(genius_url)
                if lyrics != None:
                    track_info['lyrics'] = lyrics
                    PlaylistData.append(track_info)
                else:
                    lyrics = getLyrics.getLyrics(genius_url)
                    if lyrics != None:
                        track_info['lyrics'] = lyrics
                        PlaylistData.append(track_info)
                    else:
                        lyrics = getLyrics.getLyrics(genius_url)
                        if lyrics != None:
                            track_info['lyrics'] = lyrics
                            PlaylistData.append(track_info)
                        else:
                            lyrics = getLyrics.getLyrics(genius_url)
                            if lyrics != None:
                                track_info['lyrics'] = lyrics
                                PlaylistData.append(track_info)
            print(f'Getting data for playlist {playlist_no+1}, track {track_no+1}')
    return PlaylistData

def getPlaylistCSV(playlist_data, csv_name):
    df = pd.DataFrame(playlist_data)
    df.to_csv(csv_name)