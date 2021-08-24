import getTrackData
import getPlaylistData

playlist_uri = "37i9dQZF1DXcK9HMaGBDJ4"
user_uri = "spotify"
csv_name = "test.csv"

'''
Insert playlist and user URIs here. To find URI go to the three dots/ellipses on relevant playlist/user, go to share if
for a playlist and hold ALT for the option "Copy Spotify URI" to come up. Make sure to only include text after the colon 
when copying as this is the URI. Also choose the name you want the csv to have (e.g. "90s.csv").
'''

ids = getTrackData.getTrackID(user_uri, playlist_uri)
playlist_data = getPlaylistData.getPlayistData(ids)
getPlaylistData.getPlaylistCSV(playlist_data, csv_name)

print("===============================================================================================================")
for song in playlist_data:
    print(song)
print("All done!")