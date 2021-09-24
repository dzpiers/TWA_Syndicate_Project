import getTrackData
import getPlaylistData

# Insert user and playlist URIs here (multiple if required). To find URI go to the three dots/ellipses on relevant
# playlist/user, go to share if for a playlist and hold ALT for the option "Copy Spotify URI" to come up. Make sure to
# only include text after the colon when copying. Also choose the name you want the csv to have (e.g. "90s.csv").

# Get user URIs
'''
user_uri = "spotify"
'''

# Get playlist URIs
'''
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

playlist_1970_uri = "37i9dQZF1DWXQyLTHGuTIz"
playlist_1971_uri = "37i9dQZF1DX43B4ApmA3Ee"
playlist_1972_uri = "37i9dQZF1DXaQBa5hAMckp"
playlist_1973_uri = "37i9dQZF1DX2ExTChOnD3g"
playlist_1974_uri = "37i9dQZF1DWVg6L7Yq13eC"
playlist_1975_uri = "37i9dQZF1DX3TYyWu8Zk7P"
playlist_1976_uri = "37i9dQZF1DX6rhG68uMHxl"
playlist_1977_uri = "37i9dQZF1DX26cozX10stk"
playlist_1978_uri = "37i9dQZF1DX0fr2A59qlzT"
playlist_1979_uri = "37i9dQZF1DWZLO9LcfSmxX"

playlist_1970_rock_uri = "37i9dQZF1DXe9Gx5fVy1RT"
playlist_1971_rock_uri = "37i9dQZF1DX7hJtfqsSYTk"
playlist_1972_rock_uri = "37i9dQZF1DX1zuF5yREJDe"
playlist_1973_rock_uri = "37i9dQZF1DX78DRzijRqqX"
playlist_1974_rock_uri = "37i9dQZF1DX1nxMqx6wzfy"
playlist_1975_rock_uri = "37i9dQZF1DXcZ23vu9p2EP"
playlist_1976_rock_uri = "37i9dQZF1DWY3ikieEzZoK"
playlist_1977_rock_uri = "37i9dQZF1DX6h7YXXXI74h"
playlist_1978_rock_uri = "37i9dQZF1DXcRozkBFkdf3"
playlist_1979_rock_uri = "37i9dQZF1DX0G17fJchniq"

playlist_1980_uri = "37i9dQZF1DWXbLOeOIhbc5"
playlist_1981_uri = "37i9dQZF1DX3MaR62kDrX7"
playlist_1982_uri = "37i9dQZF1DXas7qFgKz9OV"
playlist_1983_uri = "37i9dQZF1DXbE3rNuDfpVj"
playlist_1984_uri = "37i9dQZF1DX2O7iyPnNKby"
playlist_1985_uri = "37i9dQZF1DWXZ5eJ1sVtmf"
playlist_1986_uri = "37i9dQZF1DX7b12kdMQTpG"
playlist_1987_uri = "37i9dQZF1DX38yySwWsFRT"
playlist_1988_uri = "37i9dQZF1DX3MZ9dVGvZnZ"
playlist_1989_uri = "37i9dQZF1DX4qJrOCfJytN"

playlist_1987_rap_uri = "37i9dQZF1DX7FKmscS2x8B"
playlist_1988_rap_uri = "37i9dQZF1DWXL4gG0TAH6S"
playlist_1989_rap_uri = "37i9dQZF1DX5qDhvewvOhw"

playlist_1980_rock_uri = "37i9dQZF1DX8pxtTvJ2V4V"
playlist_1981_rock_uri = "37i9dQZF1DWXFHVsReRVuQ"
playlist_1982_rock_uri = "37i9dQZF1DXalVKU24eGwy"
playlist_1983_rock_uri = "37i9dQZF1DXdsCvt6F7Ona"
playlist_1984_rock_uri = "37i9dQZF1DXbeU15XEtkjO"
playlist_1985_rock_uri = "37i9dQZF1DWZj8pTzBlXEU"
playlist_1986_rock_uri = "37i9dQZF1DX57uwd7QgQqH"
playlist_1987_rock_uri = "37i9dQZF1DXbGsT3lGmSyq"
playlist_1988_rock_uri = "37i9dQZF1DX33lABaeNmpm"
playlist_1989_rock_uri = "37i9dQZF1DXblUY0xyx5hD"

playlist_1980_party_uri = "37i9dQZF1DX8lKhwdlnM5P"
playlist_1981_party_uri = "37i9dQZF1DWZ82YPqw56Ue"
playlist_1982_party_uri = "37i9dQZF1DWUOaBgFsDdue"
playlist_1983_party_uri = "37i9dQZF1DX1uZhMQcXfjn"
playlist_1984_party_uri = "37i9dQZF1DWWRox3UPRhAQ"
playlist_1985_party_uri = "37i9dQZF1DX6brVf23eXXK"
playlist_1986_party_uri = "37i9dQZF1DWTu0SBo7h8pn"
playlist_1987_party_uri = "37i9dQZF1DX71cZ31C1qtY"
playlist_1988_party_uri = "37i9dQZF1DX966qw7oVFRV"
playlist_1989_party_uri = "37i9dQZF1DX1Al1BfEn9dA"

playlist_1990_uri = "37i9dQZF1DX4joPVMjBCAo"
playlist_1991_uri = "37i9dQZF1DX6TtJfRD994c"
playlist_1992_uri = "37i9dQZF1DX9ZZCtVNwklG"
playlist_1993_uri = "37i9dQZF1DXbUFx5bcjwWK"
playlist_1994_uri = "37i9dQZF1DXbKFudfYGcmj"
playlist_1995_uri = "37i9dQZF1DXayIOFUOVODK"
playlist_1996_uri = "37i9dQZF1DWZkDl55BkJmo"
playlist_1997_uri = "37i9dQZF1DWWKd15PHZNnl"
playlist_1998_uri = "37i9dQZF1DWWmGB2u14f8m"
playlist_1999_uri = "37i9dQZF1DX4PrR66miO50"

playlist_1990_rap_uri = "37i9dQZF1DWW45yEGjKTLP"
playlist_1991_rap_uri = "37i9dQZF1DX3zKvS2WqJNQ"
playlist_1992_rap_uri = "37i9dQZF1DX8f9HUGHP1Xg"
playlist_1993_rap_uri = "37i9dQZF1DWSJEMFaWwYG8"
playlist_1994_rap_uri = "37i9dQZF1DX16FYsDCnfL9"
playlist_1995_rap_uri = "37i9dQZF1DWXV0QpJtpYUl"
playlist_1996_rap_uri = "37i9dQZF1DWZBTZq94G1cV"
playlist_1997_rap_uri = "37i9dQZF1DX9KhfaCWRHKQ"
playlist_1998_rap_uri = "37i9dQZF1DX7VcaGgd2NjX"
playlist_1999_rap_uri = "37i9dQZF1DXaTwkarURqqL"

playlist_1990_rock_uri = "37i9dQZF1DX7WKiiApnMiP"
playlist_1991_rock_uri = "37i9dQZF1DX7oIIEPSPoU3"
playlist_1992_rock_uri = "37i9dQZF1DWSOhLQd7xFdh"
playlist_1993_rock_uri = "37i9dQZF1DX0yWpalsk2hI"
playlist_1994_rock_uri = "37i9dQZF1DXb7TP3hnjz42"
playlist_1995_rock_uri = "37i9dQZF1DXd9YOz6k1Yx4"
playlist_1996_rock_uri = "37i9dQZF1DX4jSCizAzbyM"
playlist_1997_rock_uri = "37i9dQZF1DXe3xQ87w7k3M"
playlist_1998_rock_uri = "37i9dQZF1DWZPqHZ7Q4Gis"
playlist_1999_rock_uri = "37i9dQZF1DWV4tgsIXfwye"

playlist_1990_party_uri = "37i9dQZF1DXdnkV80yv93x"
playlist_1991_party_uri = "37i9dQZF1DWUAlPk7Wg6Rp"
playlist_1992_party_uri = "37i9dQZF1DX8Zwbqfqz39o"
playlist_1993_party_uri = "37i9dQZF1DX2isOEVu6IQC"
playlist_1994_party_uri = "37i9dQZF1DX26eeMjJtcCh"
playlist_1995_party_uri = "37i9dQZF1DXbYSzUjUMKzC"
playlist_1996_party_uri = "37i9dQZF1DWU5Qb1HUtZCA"
playlist_1997_party_uri = "37i9dQZF1DXdqLvocLoRhO"
playlist_1998_party_uri = "37i9dQZF1DX5msvI3CypeA"
playlist_1999_party_uri = "37i9dQZF1DXdmA4leK8vrY"

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

playlist_2000_rock_uri = "37i9dQZF1DX6rsDrBNGuWW"
playlist_2001_rock_uri = "37i9dQZF1DX9vRGeh98xcN"
playlist_2002_rock_uri = "37i9dQZF1DWXHPEQuQqSH9"
playlist_2003_rock_uri = "37i9dQZF1DXcYAgq4oLyJ4"
playlist_2004_rock_uri = "37i9dQZF1DX0AtsZ32JWUn"
playlist_2005_rock_uri = "37i9dQZF1DWYtIgspfyIDd"
playlist_2006_rock_uri = "37i9dQZF1DX2hfIBBY7Put"
playlist_2007_rock_uri = "37i9dQZF1DX1k65azGVY2p"
playlist_2008_rock_uri = "37i9dQZF1DX8vmVOT0h7vf"
playlist_2009_rock_uri = "37i9dQZF1DX5ew6WQQfG5f"

playlist_2000_party_uri = "37i9dQZF1DXc7Rb7Sc87GT"
playlist_2001_party_uri = "37i9dQZF1DX9Mwebj7agu9"
playlist_2002_party_uri = "37i9dQZF1DWYRXLvPEeDZQ"
playlist_2003_party_uri = "37i9dQZF1DX8ZymkpfFYdY"
playlist_2004_party_uri = "37i9dQZF1DX1fPO1jgwUdk"
playlist_2005_party_uri = "37i9dQZF1DX5PkwA2E2A23"
playlist_2006_party_uri = "37i9dQZF1DWZtWY5ulmJA5"
playlist_2007_party_uri = "37i9dQZF1DX7wcpyXnyv6H"
playlist_2008_party_uri = "37i9dQZF1DX3HPrk9Aq9xl"
playlist_2009_party_uri = "37i9dQZF1DWXS9GPFGA0OX"

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

playlist_2010_rock_uri = "37i9dQZF1DX82Ifqec3rkg"
playlist_2011_rock_uri = "37i9dQZF1DX4KTujSwyTmQ"
playlist_2012_rock_uri = "37i9dQZF1DWZ3ZJIiIfKXn"
playlist_2013_rock_uri = "37i9dQZF1DWSEJi7q7m7b7"
playlist_2014_rock_uri = "37i9dQZF1DX2ieLsD6FsU8"
playlist_2015_rock_uri = "37i9dQZF1DWUgWcdgqYurj"
playlist_2016_rock_uri = "37i9dQZF1DWXxHUoxKljZ1"
playlist_2017_rock_uri = "37i9dQZF1DX1HUp3K8hq5o"
playlist_2018_rock_uri = "37i9dQZF1DWZFav20JcPkX"
playlist_2019_rock_uri = "37i9dQZF1DXbfwGuHFlleD"

playlist_2010_party_uri = "37i9dQZF1DX7kWRaihZUiq"
playlist_2011_party_uri = "37i9dQZF1DX84Y3suEuIzI"
playlist_2012_party_uri = "37i9dQZF1DX8c5G0q1PWqI"
playlist_2013_party_uri = "37i9dQZF1DXdNkjKPeTeO0"
playlist_2014_party_uri = "37i9dQZF1DX3Yd4VPj7JIJ"
playlist_2015_party_uri = "37i9dQZF1DXcYdNBfH2DzY"
playlist_2016_party_uri = "37i9dQZF1DWUoOVVVaQYGO"
playlist_2017_party_uri = "37i9dQZF1DXcGoNUUaNbIj"
playlist_2018_party_uri = "37i9dQZF1DWWAcJDz94rMo"
playlist_2019_party_uri = "37i9dQZF1DX2etMgwPjO92"
'''

# Get list of ids for each playlist
'''
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

ids_1970 = getTrackData.getTrackID(user_uri, playlist_1970_uri)
ids_1971 = getTrackData.getTrackID(user_uri, playlist_1971_uri)
ids_1972 = getTrackData.getTrackID(user_uri, playlist_1972_uri)
ids_1973 = getTrackData.getTrackID(user_uri, playlist_1973_uri)
ids_1974 = getTrackData.getTrackID(user_uri, playlist_1974_uri)
ids_1975 = getTrackData.getTrackID(user_uri, playlist_1975_uri)
ids_1976 = getTrackData.getTrackID(user_uri, playlist_1976_uri)
ids_1977 = getTrackData.getTrackID(user_uri, playlist_1977_uri)
ids_1978 = getTrackData.getTrackID(user_uri, playlist_1978_uri)
ids_1979 = getTrackData.getTrackID(user_uri, playlist_1979_uri)

ids_1970_rock = getTrackData.getTrackID(user_uri, playlist_1970_rock_uri)
ids_1971_rock = getTrackData.getTrackID(user_uri, playlist_1971_rock_uri)
ids_1972_rock = getTrackData.getTrackID(user_uri, playlist_1972_rock_uri)
ids_1973_rock = getTrackData.getTrackID(user_uri, playlist_1973_rock_uri)
ids_1974_rock = getTrackData.getTrackID(user_uri, playlist_1974_rock_uri)
ids_1975_rock = getTrackData.getTrackID(user_uri, playlist_1975_rock_uri)
ids_1976_rock = getTrackData.getTrackID(user_uri, playlist_1976_rock_uri)
ids_1977_rock = getTrackData.getTrackID(user_uri, playlist_1977_rock_uri)
ids_1978_rock = getTrackData.getTrackID(user_uri, playlist_1978_rock_uri)
ids_1979_rock = getTrackData.getTrackID(user_uri, playlist_1979_rock_uri)

ids_1980 = getTrackData.getTrackID(user_uri, playlist_1980_uri)
ids_1981 = getTrackData.getTrackID(user_uri, playlist_1981_uri)
ids_1982 = getTrackData.getTrackID(user_uri, playlist_1982_uri)
ids_1983 = getTrackData.getTrackID(user_uri, playlist_1983_uri)
ids_1984 = getTrackData.getTrackID(user_uri, playlist_1984_uri)
ids_1985 = getTrackData.getTrackID(user_uri, playlist_1985_uri)
ids_1986 = getTrackData.getTrackID(user_uri, playlist_1986_uri)
ids_1987 = getTrackData.getTrackID(user_uri, playlist_1987_uri)
ids_1988 = getTrackData.getTrackID(user_uri, playlist_1988_uri)
ids_1989 = getTrackData.getTrackID(user_uri, playlist_1989_uri)

ids_1987_rap = getTrackData.getTrackID(user_uri, playlist_1987_rap_uri)
ids_1988_rap = getTrackData.getTrackID(user_uri, playlist_1988_rap_uri)
ids_1989_rap = getTrackData.getTrackID(user_uri, playlist_1989_rap_uri)

ids_1980_rock = getTrackData.getTrackID(user_uri, playlist_1980_rock_uri)
ids_1981_rock = getTrackData.getTrackID(user_uri, playlist_1981_rock_uri)
ids_1982_rock = getTrackData.getTrackID(user_uri, playlist_1982_rock_uri)
ids_1983_rock = getTrackData.getTrackID(user_uri, playlist_1983_rock_uri)
ids_1984_rock = getTrackData.getTrackID(user_uri, playlist_1984_rock_uri)
ids_1985_rock = getTrackData.getTrackID(user_uri, playlist_1985_rock_uri)
ids_1986_rock = getTrackData.getTrackID(user_uri, playlist_1986_rock_uri)
ids_1987_rock = getTrackData.getTrackID(user_uri, playlist_1987_rock_uri)
ids_1988_rock = getTrackData.getTrackID(user_uri, playlist_1988_rock_uri)
ids_1989_rock = getTrackData.getTrackID(user_uri, playlist_1989_rock_uri)

ids_1980_party = getTrackData.getTrackID(user_uri, playlist_1980_party_uri)
ids_1981_party = getTrackData.getTrackID(user_uri, playlist_1981_party_uri)
ids_1982_party = getTrackData.getTrackID(user_uri, playlist_1982_party_uri)
ids_1983_party = getTrackData.getTrackID(user_uri, playlist_1983_party_uri)
ids_1984_party = getTrackData.getTrackID(user_uri, playlist_1984_party_uri)
ids_1985_party = getTrackData.getTrackID(user_uri, playlist_1985_party_uri)
ids_1986_party = getTrackData.getTrackID(user_uri, playlist_1986_party_uri)
ids_1987_party = getTrackData.getTrackID(user_uri, playlist_1987_party_uri)
ids_1988_party = getTrackData.getTrackID(user_uri, playlist_1988_party_uri)
ids_1989_party = getTrackData.getTrackID(user_uri, playlist_1989_party_uri)

ids_1990 = getTrackData.getTrackID(user_uri, playlist_1990_uri)
ids_1991 = getTrackData.getTrackID(user_uri, playlist_1991_uri)
ids_1992 = getTrackData.getTrackID(user_uri, playlist_1992_uri)
ids_1993 = getTrackData.getTrackID(user_uri, playlist_1993_uri)
ids_1994 = getTrackData.getTrackID(user_uri, playlist_1994_uri)
ids_1995 = getTrackData.getTrackID(user_uri, playlist_1995_uri)
ids_1996 = getTrackData.getTrackID(user_uri, playlist_1996_uri)
ids_1997 = getTrackData.getTrackID(user_uri, playlist_1997_uri)
ids_1998 = getTrackData.getTrackID(user_uri, playlist_1998_uri)
ids_1999 = getTrackData.getTrackID(user_uri, playlist_1999_uri)

ids_1990_rap = getTrackData.getTrackID(user_uri, playlist_1990_rap_uri)
ids_1991_rap = getTrackData.getTrackID(user_uri, playlist_1991_rap_uri)
ids_1992_rap = getTrackData.getTrackID(user_uri, playlist_1992_rap_uri)
ids_1993_rap = getTrackData.getTrackID(user_uri, playlist_1993_rap_uri)
ids_1994_rap = getTrackData.getTrackID(user_uri, playlist_1994_rap_uri)
ids_1995_rap = getTrackData.getTrackID(user_uri, playlist_1995_rap_uri)
ids_1996_rap = getTrackData.getTrackID(user_uri, playlist_1996_rap_uri)
ids_1997_rap = getTrackData.getTrackID(user_uri, playlist_1997_rap_uri)
ids_1998_rap = getTrackData.getTrackID(user_uri, playlist_1998_rap_uri)
ids_1999_rap = getTrackData.getTrackID(user_uri, playlist_1999_rap_uri)

ids_1990_rock = getTrackData.getTrackID(user_uri, playlist_1990_rock_uri)
ids_1991_rock = getTrackData.getTrackID(user_uri, playlist_1991_rock_uri)
ids_1992_rock = getTrackData.getTrackID(user_uri, playlist_1992_rock_uri)
ids_1993_rock = getTrackData.getTrackID(user_uri, playlist_1993_rock_uri)
ids_1994_rock = getTrackData.getTrackID(user_uri, playlist_1994_rock_uri)
ids_1995_rock = getTrackData.getTrackID(user_uri, playlist_1995_rock_uri)
ids_1996_rock = getTrackData.getTrackID(user_uri, playlist_1996_rock_uri)
ids_1997_rock = getTrackData.getTrackID(user_uri, playlist_1997_rock_uri)
ids_1998_rock = getTrackData.getTrackID(user_uri, playlist_1998_rock_uri)
ids_1999_rock = getTrackData.getTrackID(user_uri, playlist_1999_rock_uri)

ids_1990_party = getTrackData.getTrackID(user_uri, playlist_1990_party_uri)
ids_1991_party = getTrackData.getTrackID(user_uri, playlist_1991_party_uri)
ids_1992_party = getTrackData.getTrackID(user_uri, playlist_1992_party_uri)
ids_1993_party = getTrackData.getTrackID(user_uri, playlist_1993_party_uri)
ids_1994_party = getTrackData.getTrackID(user_uri, playlist_1994_party_uri)
ids_1995_party = getTrackData.getTrackID(user_uri, playlist_1995_party_uri)
ids_1996_party = getTrackData.getTrackID(user_uri, playlist_1996_party_uri)
ids_1997_party = getTrackData.getTrackID(user_uri, playlist_1997_party_uri)
ids_1998_party = getTrackData.getTrackID(user_uri, playlist_1998_party_uri)
ids_1999_party = getTrackData.getTrackID(user_uri, playlist_1999_party_uri)

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

ids_2000_rock = getTrackData.getTrackID(user_uri, playlist_2000_rock_uri)
ids_2001_rock = getTrackData.getTrackID(user_uri, playlist_2001_rock_uri)
ids_2002_rock = getTrackData.getTrackID(user_uri, playlist_2002_rock_uri)
ids_2003_rock = getTrackData.getTrackID(user_uri, playlist_2003_rock_uri)
ids_2004_rock = getTrackData.getTrackID(user_uri, playlist_2004_rock_uri)
ids_2005_rock = getTrackData.getTrackID(user_uri, playlist_2005_rock_uri)
ids_2006_rock = getTrackData.getTrackID(user_uri, playlist_2006_rock_uri)
ids_2007_rock = getTrackData.getTrackID(user_uri, playlist_2007_rock_uri)
ids_2008_rock = getTrackData.getTrackID(user_uri, playlist_2008_rock_uri)
ids_2009_rock = getTrackData.getTrackID(user_uri, playlist_2009_rock_uri)

ids_2000_party = getTrackData.getTrackID(user_uri, playlist_2000_party_uri)
ids_2001_party = getTrackData.getTrackID(user_uri, playlist_2001_party_uri)
ids_2002_party = getTrackData.getTrackID(user_uri, playlist_2002_party_uri)
ids_2003_party = getTrackData.getTrackID(user_uri, playlist_2003_party_uri)
ids_2004_party = getTrackData.getTrackID(user_uri, playlist_2004_party_uri)
ids_2005_party = getTrackData.getTrackID(user_uri, playlist_2005_party_uri)
ids_2006_party = getTrackData.getTrackID(user_uri, playlist_2006_party_uri)
ids_2007_party = getTrackData.getTrackID(user_uri, playlist_2007_party_uri)
ids_2008_party = getTrackData.getTrackID(user_uri, playlist_2008_party_uri)
ids_2009_party = getTrackData.getTrackID(user_uri, playlist_2009_party_uri)

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

ids_2010_rock = getTrackData.getTrackID(user_uri, playlist_2010_rock_uri)
ids_2011_rock = getTrackData.getTrackID(user_uri, playlist_2011_rock_uri)
ids_2012_rock = getTrackData.getTrackID(user_uri, playlist_2012_rock_uri)
ids_2013_rock = getTrackData.getTrackID(user_uri, playlist_2013_rock_uri)
ids_2014_rock = getTrackData.getTrackID(user_uri, playlist_2014_rock_uri)
ids_2015_rock = getTrackData.getTrackID(user_uri, playlist_2015_rock_uri)
ids_2016_rock = getTrackData.getTrackID(user_uri, playlist_2016_rock_uri)
ids_2017_rock = getTrackData.getTrackID(user_uri, playlist_2017_rock_uri)
ids_2018_rock = getTrackData.getTrackID(user_uri, playlist_2018_rock_uri)
ids_2019_rock = getTrackData.getTrackID(user_uri, playlist_2019_rock_uri)

ids_2010_party = getTrackData.getTrackID(user_uri, playlist_2010_party_uri)
ids_2011_party = getTrackData.getTrackID(user_uri, playlist_2011_party_uri)
ids_2012_party = getTrackData.getTrackID(user_uri, playlist_2012_party_uri)
ids_2013_party = getTrackData.getTrackID(user_uri, playlist_2013_party_uri)
ids_2014_party = getTrackData.getTrackID(user_uri, playlist_2014_party_uri)
ids_2015_party = getTrackData.getTrackID(user_uri, playlist_2015_party_uri)
ids_2016_party = getTrackData.getTrackID(user_uri, playlist_2016_party_uri)
ids_2017_party = getTrackData.getTrackID(user_uri, playlist_2017_party_uri)
ids_2018_party = getTrackData.getTrackID(user_uri, playlist_2018_party_uri)
ids_2019_party = getTrackData.getTrackID(user_uri, playlist_2019_party_uri)
'''

# Create dataframe for list of ids (as many as you want)
playlist_data = getPlaylistData.getPlaylistData(ids)

# Choose csv name for output
csv_name = "test.csv"

# Produce csv
getPlaylistData.getPlaylistCSV(playlist_data, csv_name)

print("===============================================================================================================")
for song in playlist_data:
    print(song)
print(len(playlist_data), "songs written to csv")
print("All done!")