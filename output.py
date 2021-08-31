import getTrackData
import getPlaylistData

'''
Insert user and playlist URIs here (multiple if required). To find URI go to the three dots/ellipses on relevant 
playlist/user, go to share if for a playlist and hold ALT for the option "Copy Spotify URI" to come up. Make sure to 
only include text after the colon when copying. Also choose the name you want the csv to have (e.g. "90s.csv").
'''

user_uri = "spotify"

playlist_50s_uri1 = "37i9dQZF1DWSV3Tk4GO2fq"
playlist_50s_uri2 = "37i9dQZF1DWXcg95telZlE"
playlist_50s_uri3 = "37i9dQZF1DWSwFS0Z6E1ep"
playlist_50s_uri4 = "37i9dQZF1DX3EgfgehUd1l"
playlist_50s_uri5 = "37i9dQZF1DWWnpcjfCqaW0"
playlist_50s_uri6 = "2SwjQPegrTTYaOsWQrwhMe"
playlist_50s_uri7 = "37i9dQZF1EQqMLgxRRiCOd"
playlist_50s_uri8 = "37i9dQZF1DWUGhrXBsyMVJ"
playlist_50s_uri9 = "37i9dQZF1DXe2fHCBYbwN7"
playlist_50s_uri10 = "2mcSrE5xOITK0hD5m4aNRu"
playlist_50s_uri11 = "7d2ikFYCf3pBPIlNCdGz20"

playlist_60s_uri1 = "37i9dQZF1DXaKIA8E7WcJj"
playlist_60s_uri2 = "37i9dQZF1DWWzBc3TOlaAV"
playlist_60s_uri3 = "37i9dQZF1DX5qNE4zrflL7"
playlist_60s_uri4 = "37i9dQZF1DWYzKmy0vGGcY"
playlist_60s_uri5 = "37i9dQZF1DX3AdAEX3vkB1"
playlist_60s_uri6 = "37i9dQZF1DXdefH9jYbLNT"
playlist_60s_uri7 = "37i9dQZF1DX7CGYgLhqwu5"
playlist_60s_uri8 = "37i9dQZF1EQoHemmkbENDL"
playlist_60s_uri9 = "37i9dQZF1DWVKGowYB4WMF"
playlist_60s_uri10 = "32f7ctSV6ZLppG27q4WIya"
playlist_60s_uri11 = "0KU1eeB1eEFGFz3QWi72q8"
playlist_60s_uri12 = "27ddjXFvG3EPtdB0IoyHfN"
playlist_60s_uri13 = "7KG5vnSOvT5HXZB9enR63r"

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

playlist_2000_rap_uri = "37i9dQZF1DX38t16fuNXJJ"
playlist_2001_rap_uri = "37i9dQZF1DX84LhXlEFtT2"
playlist_2002_rap_uri = "37i9dQZF1DX3CFCcirpUyC"
playlist_2003_rap_uri = "37i9dQZF1DWXODx4qTnKLo"
playlist_2004_rap_uri = "37i9dQZF1DWV5Yt9QQ1nyU"
playlist_2005_rap_uri = "37i9dQZF1DWZVgxgOsMmRi"
playlist_2006_rap_uri = "37i9dQZF1DX03tzurzdSBW"
playlist_2007_rap_uri = "37i9dQZF1DX6agKta0oCzd"
playlist_2008_rap_uri = "37i9dQZF1DXccZmQhlQC8y"
playlist_2009_rap_uri = "37i9dQZF1DWX2EeJTd5hhM"

playlist_2010_uri = "37i9dQZF1DXc6IFF23C9jj"
playlist_2011_uri = "37i9dQZF1DXcagnSNtrGuJ"
playlist_2012_uri = "37i9dQZF1DX0yEZaMOXna3"
playlist_2013_uri = "37i9dQZF1DX3Sp0P28SIer"
playlist_2014_uri = "37i9dQZF1DX0h0QnLkMBl4"
playlist_2015_uri = "37i9dQZF1DX9ukdrXQLJGZ"
playlist_2016_uri = "37i9dQZF1DX8XZ6AUo9R4R"
playlist_2017_uri = "37i9dQZF1DWTE7dVUebpUW"
playlist_2018_uri = "37i9dQZF1DXe2bobNYDtW8"
playlist_2019_uri = "37i9dQZF1DWVRSukIED0e9"

playlist_2010_rap_uri = "37i9dQZF1DWSMW5YBCZisa"
playlist_2011_rap_uri = "37i9dQZF1DX3D1xvN8LjbH"
playlist_2012_rap_uri = "37i9dQZF1DX92DV8EP7bwz"
playlist_2013_rap_uri = "37i9dQZF1DWSWuGRBgXzLE"
playlist_2014_rap_uri = "37i9dQZF1DWTOgTfzyNaei"
playlist_2015_rap_uri = "37i9dQZF1DXcqWbpeXswkc"
playlist_2016_rap_uri = "37i9dQZF1DWZSCnPqfx5XX"
playlist_2017_rap_uri = "37i9dQZF1DWUUeLChAs7Px"
playlist_2018_rap_uri = "37i9dQZF1DWVXS1PI6Zs44"
playlist_2019_rap_uri = "37i9dQZF1DWZiyat8YCzeB"

'Choose csv name for output'
csv_name = "1960s.csv"

'Get list of ids for each playlist'
ids_50s1 = getTrackData.getTrackID(user_uri, playlist_50s_uri1)
ids_50s2 = getTrackData.getTrackID(user_uri, playlist_50s_uri2)
ids_50s3 = getTrackData.getTrackID(user_uri, playlist_50s_uri3)
ids_50s4 = getTrackData.getTrackID(user_uri, playlist_50s_uri4)
ids_50s5 = getTrackData.getTrackID(user_uri, playlist_50s_uri5)
ids_50s6 = getTrackData.getTrackID("michemike1", playlist_50s_uri6)
ids_50s7 = getTrackData.getTrackID(user_uri, playlist_50s_uri7)
ids_50s8 = getTrackData.getTrackID(user_uri, playlist_50s_uri8)
ids_50s9 = getTrackData.getTrackID(user_uri, playlist_50s_uri9)
ids_50s10 = getTrackData.getTrackID("nickheinis", playlist_50s_uri10)
ids_50s11 = getTrackData.getTrackID("brendaolivas09", playlist_50s_uri11)

ids_60s1 = getTrackData.getTrackID(user_uri, playlist_60s_uri1)
ids_60s2 = getTrackData.getTrackID(user_uri, playlist_60s_uri2)
ids_60s3 = getTrackData.getTrackID(user_uri, playlist_60s_uri3)
ids_60s4 = getTrackData.getTrackID(user_uri, playlist_60s_uri4)
ids_60s5 = getTrackData.getTrackID(user_uri, playlist_60s_uri5)
ids_60s6 = getTrackData.getTrackID(user_uri, playlist_60s_uri6)
ids_60s7 = getTrackData.getTrackID(user_uri, playlist_60s_uri7)
ids_60s8 = getTrackData.getTrackID(user_uri, playlist_60s_uri8)
ids_60s9 = getTrackData.getTrackID(user_uri, playlist_60s_uri9)
ids_60s10 = getTrackData.getTrackID("listanauta", playlist_60s_uri10)
ids_60s11 = getTrackData.getTrackID("brendenfar.17", playlist_60s_uri11)
ids_60s12 = getTrackData.getTrackID("124245169", playlist_60s_uri12)
ids_60s13 = getTrackData.getTrackID("teage03", playlist_60s_uri13)

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

ids_2000_rap = getTrackData.getTrackID(user_uri, playlist_2000_rap_uri)
ids_2001_rap = getTrackData.getTrackID(user_uri, playlist_2001_rap_uri)
ids_2002_rap = getTrackData.getTrackID(user_uri, playlist_2002_rap_uri)
ids_2003_rap = getTrackData.getTrackID(user_uri, playlist_2003_rap_uri)
ids_2004_rap = getTrackData.getTrackID(user_uri, playlist_2004_rap_uri)
ids_2005_rap = getTrackData.getTrackID(user_uri, playlist_2005_rap_uri)
ids_2006_rap = getTrackData.getTrackID(user_uri, playlist_2006_rap_uri)
ids_2007_rap = getTrackData.getTrackID(user_uri, playlist_2007_rap_uri)
ids_2008_rap = getTrackData.getTrackID(user_uri, playlist_2008_rap_uri)
ids_2009_rap = getTrackData.getTrackID(user_uri, playlist_2009_rap_uri)

ids_2010 = getTrackData.getTrackID(user_uri, playlist_2010_uri)
ids_2011 = getTrackData.getTrackID(user_uri, playlist_2011_uri)
ids_2012 = getTrackData.getTrackID(user_uri, playlist_2012_uri)
ids_2013 = getTrackData.getTrackID(user_uri, playlist_2013_uri)
ids_2014 = getTrackData.getTrackID(user_uri, playlist_2014_uri)
ids_2015 = getTrackData.getTrackID(user_uri, playlist_2015_uri)
ids_2016 = getTrackData.getTrackID(user_uri, playlist_2016_uri)
ids_2017 = getTrackData.getTrackID(user_uri, playlist_2017_uri)
ids_2018 = getTrackData.getTrackID(user_uri, playlist_2018_uri)
ids_2019 = getTrackData.getTrackID(user_uri, playlist_2019_uri)

ids_2010_rap = getTrackData.getTrackID(user_uri, playlist_2010_rap_uri)
ids_2011_rap = getTrackData.getTrackID(user_uri, playlist_2011_rap_uri)
ids_2012_rap = getTrackData.getTrackID(user_uri, playlist_2012_rap_uri)
ids_2013_rap = getTrackData.getTrackID(user_uri, playlist_2013_rap_uri)
ids_2014_rap = getTrackData.getTrackID(user_uri, playlist_2014_rap_uri)
ids_2015_rap = getTrackData.getTrackID(user_uri, playlist_2015_rap_uri)
ids_2016_rap = getTrackData.getTrackID(user_uri, playlist_2016_rap_uri)
ids_2017_rap = getTrackData.getTrackID(user_uri, playlist_2017_rap_uri)
ids_2018_rap = getTrackData.getTrackID(user_uri, playlist_2018_rap_uri)
ids_2019_rap = getTrackData.getTrackID(user_uri, playlist_2019_rap_uri)


'Create dataframe for list of ids (as many as you want)'
playlist_data = getPlaylistData.getPlayistData(ids_60s1, ids_60s2, ids_60s3, ids_60s4, ids_60s5, ids_60s6, ids_60s7, ids_60s8, ids_60s9, ids_60s10, ids_60s11, ids_60s12, ids_60s13)

'Produce csv'
getPlaylistData.getPlaylistCSV(playlist_data, csv_name)

print("===============================================================================================================")
for song in playlist_data:
    print(song)
print(len(playlist_data), "songs written to csv")
print("All done!")