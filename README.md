# spotify-top-200-dataset
Spotify Charts weekly top 200 songs between 2017~2021 in global dataset &amp; api extraction codes

## ~~ about dataset ~~
spotify weekly top 200 songs between 2017-2021 in global.
50.000 rows
39 columns
1.950.000 items
10 data types (char, tinyint, varchar, bool, date, smallint, decimal, blob,  float, int)
columns.

## ~~ columns ~~
track_id(char[22]) : spotify id for the track
track_name(varchar[666]) : name of the track
track_popularity(double[3, 2]) : popularity of the track calculated by spotify
track_number(u-tinyint) : track’s index relative to its album
album_id(char[22]) : spotify id for the album that the track is from
album_name(varchar[666]) : name of the album that the track is from
album_img(blob) : link to the cover image of album that the track is from
album_type(varchar[10]) : type of the album (eg. single, album)
album_label(varchar[666]) : track’s record label
album_track_number(u-tinyint) : number of the tracks in the album that the track is from
album_popularity(double[3,2]) : popularity of the album calculated by spotify
artist_num(u-tinyint) : number of artists in the track
artist_names(varchar[666]) : names of all artists who participated in the track (separated by comma)
artist_id(char[22]) : spotify artist id for the artist_individual
artist_name(varchar[666]) : one of the artists who participated in the track (tracks with multiple artists are split into separate rows for each artist)
artist_img(char[40]) : link to the artist_individual’s image
artist_followers(u-int) : follower amount of artist
artist_popularity(decimal[3,2]) : popularity of the artist calculated by spotify
artist_genres(varchar[666]) : artist’s genres
rank(u-tinyint) : ranking of the track on the chart
week(date) : end of week the track was in charts as date format
collab(bool) : if the participation of the track is multiple or not (0 if there is only one artist, else 1)
explicit(bool) : explicit situation of the track
release_date(date) : release date of the album (thus track)
danceability(double[4, 3]) : Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

energy(double[4, 3]) : Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.

key(tinyint) : The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
>= -1<= 11

mode(bool) : Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.

time_signature(u-tinyint) : 

loudness(float) : The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.

speechiness(decimal[5,4]) : Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.

acousticness(float) : A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.

instrumentalness(float) : Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.

liveness(decimal[5,4]) : Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.

valence(decimal[5,4]) : A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

tempo(float) : The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.

duration(u-int) : The duration of the track in milliseconds.
pivot(bool) : when multiple artists are split into separate rows, this value takes 0 for the first artist and 1 for the rest

pivot(bool) : 0 for the first artist featured in the track, 1 for rest

streams(u-int) : number of streams in that week

## ~~ references ~~
spotify api docs~ [developers spotify](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features)

pivot~ [bartomiejczyewski's spotify top 200](https://www.kaggle.com/datasets/bartomiejczyewski/spotify-top-200-weekly-global-20172021)

idea~ [yelexa's spotify top 200](https://www.kaggle.com/datasets/yelexa/spotify200)

github~ [my github page for the dataset](https://github.com/younver/spotify-top-200-dataset)
