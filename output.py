import getTrackData
import getPlaylistData

'''
Insert user and playlist URIs here (multiple if required). To find URI go to the three dots/ellipses on relevant 
playlist/user, go to share if for a playlist and hold ALT for the option "Copy Spotify URI" to come up. Make sure to 
only include text after the colon when copying. Also choose the name you want the csv to have (e.g. "90s.csv").
'''

user_uri = "spotify"

playlist_2000_uri = "37i9dQZF1DWUZv12GM5cFk"
playlist_2001_uri = "37i9dQZF1DX9Ol4tZWPH6V"
playlist_2002_uri = "37i9dQZF1DX0P7PzzKwEKl"
playlist_2003_uri = "37i9dQZF1DXaW8fzPh9b08"
playlist_2004_uri = "37i9dQZF1DWTWdbR13PQYH"
playlist_2005_uri = "37i9dQZF1DWWzQTBs5BHX9"
playlist_2006_uri = "37i9dQZF1DX1vSJnMeoy3V"
playlist_2007_uri = "37i9dQZF1DX3j9EYdzv2N9"
playlist_2008_uri = "37i9dQZF1DWYuGZUE4XQXm"
playlist_2009_uri = "37i9dQZF1DX4UkKv8ED8jp"

'Choose csv name for output'
csv_name = "test.csv"

'Get list of ids for each playlist'
ids_2000 = getTrackData.getTrackID(user_uri, playlist_2000_uri)
ids_2001 = getTrackData.getTrackID(user_uri, playlist_2001_uri)
ids_2002 = getTrackData.getTrackID(user_uri, playlist_2002_uri)
ids_2003 = getTrackData.getTrackID(user_uri, playlist_2003_uri)
ids_2004 = getTrackData.getTrackID(user_uri, playlist_2004_uri)
ids_2005 = getTrackData.getTrackID(user_uri, playlist_2005_uri)
ids_2006 = getTrackData.getTrackID(user_uri, playlist_2006_uri)
ids_2007 = getTrackData.getTrackID(user_uri, playlist_2007_uri)
ids_2008 = getTrackData.getTrackID(user_uri, playlist_2008_uri)
ids_2009 = getTrackData.getTrackID(user_uri, playlist_2009_uri)


'Create dataframe for list of ids (as many as you want)'
playlist_data = getPlaylistData.getPlayistData(ids_2000, ids_2001, ids_2002, ids_2003, ids_2004, ids_2005, ids_2006, ids_2007, ids_2008, ids_2009)

'Produce csv'
getPlaylistData.getPlaylistCSV(playlist_data, csv_name)

print("===============================================================================================================")
for song in playlist_data:
    print(song)
print(len(playlist_data), "songs written to csv")
print("All done!")