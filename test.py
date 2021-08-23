import getTrackData
import getPlaylistData

test_playlist_uri = "3odNjkuC77flx2Aob21Ejp"
test_uri = "dhruv.piers"
test_csv = "test.csv"

test_id = getTrackData.getTrackID(test_uri, test_playlist_uri)
test = getPlaylistData.getPlayistData(test_id)
getPlaylistData.getPlaylistCSV(test, test_csv)

print("===============================================================================================================")
print("===============================================================================================================")
print("===============================================================================================================")