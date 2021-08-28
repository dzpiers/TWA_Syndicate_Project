import getTrackData
import getPlaylistData

'''
Insert user and playlist URIs here (multiple if required). To find URI go to the three dots/ellipses on relevant 
playlist/user, go to share if for a playlist and hold ALT for the option "Copy Spotify URI" to come up. Make sure to 
only include text after the colon when copying. Also choose the name you want the csv to have (e.g. "90s.csv").
'''

user_uri = "spotify"
playlist_2010_uri = "37i9dQZF1DXc6IFF23C9jj"
playlist_2011_uri = "37i9dQZF1DXcagnSNtrGuJ"
csv_name = "test.csv"

'Get list of ids for each playlist'
ids_1990 = getTrackData.getTrackID(user_uri, playlist_2010_uri)
ids_1991 = getTrackData.getTrackID(user_uri, playlist_2011_uri)

'Create dataframe for list of ids (as many as you want)'
playlist_data = getPlaylistData.getPlayistData(ids_1990, ids_1991)

'Produce csv'
getPlaylistData.getPlaylistCSV(playlist_data, csv_name)

print("===============================================================================================================")
for song in playlist_data:
    print(song)
print("All done!")