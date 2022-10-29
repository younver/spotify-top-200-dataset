# spotify-top-200-dataset
Spotify Charts weekly top 200 songs between 2017~2021 in global dataset &amp; api extraction codes<br/>

## ~~ about dataset ~~
spotify weekly top 200 songs between 2017-2021 in global.<br/>
74.661 rows<br/>
40 columns<br/>
2.986.440 items<br/>
10 data types (char, tinyint, varchar, bool, date, smallint, decimal, blob,  float, int)
columns.<br/>

## ~~ columns ~~
track_id(char[22]) : spotify id for the track<br/>
track_name(varchar[666]) : name of the track<br/>
track_popularity(double[3, 2]) : popularity of the track calculated by spotify<br/>
track_number(u-tinyint) : track’s index relative to its album<br/>
album_id(char[22]) : spotify id for the album that the track is from<br/>
album_name(varchar[666]) : name of the album that the track is from<br/>
album_img(blob) : link to the cover image of album that the track is from<br/>
album_type(varchar[10]) : type of the album (eg. single, album)<br/>
album_label(varchar[666]) : track’s record label<br/>
album_track_number(u-tinyint) : number of the tracks in the album that the track is from<br/>
album_popularity(double[3,2]) : popularity of the album calculated by spotify<br/>
artist_num(u-tinyint) : number of artists in the track<br/>
artist_names(varchar[666]) : names of all artists who participated in the track (separated by comma)<br/>
artist_id(char[22]) : spotify artist id for the artist_individual<br/>
artist_name(varchar[666]) : one of the artists who participated in the track (tracks with multiple artists are split into separate rows for each artist)<br/>
artist_img(char[40]) : link to the artist_individual’s image<br/>
artist_followers(u-int) : follower amount of artist<br/>
artist_popularity(decimal[3,2]) : popularity of the artist calculated by spotify<br/>
artist_genres(varchar[666]) : artist’s genres<br/>
rank(u-tinyint) : ranking of the track on the chart<br/>
week(date) : end of week the track was in charts as date format<br/>
streams(u-int) : number of streams in that week<br/>
collab(bool) : if the participation of the track is multiple or not (0 if there is only one artist, else 1)<br/>
explicit(bool) : explicit situation of the track<br/>
release_date(date) : release date of the album (thus track)<br/>
danceability(double[4, 3]), energy(double[4, 3]), key(tinyint), mode(bool), time_signature(u-tinyint), loudness(float), speechiness(decimal[5,4]), acousticness(float), instrumentalness(float), liveness(decimal[5,4]), valence(decimal[5,4]), tempo(float), duration(u-int) : [Spotify API Reference](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features)<br/>
pivot(bool) : when multiple artists are split into separate rows, this value takes 0 for the first artist and 1 for the rest

## ~~ references ~~
spotify api docs~ [developers spotify](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features)

pivot~ [bartomiejczyewski's spotify top 200](https://www.kaggle.com/datasets/bartomiejczyewski/spotify-top-200-weekly-global-20172021)

idea~ [yelexa's spotify top 200](https://www.kaggle.com/datasets/yelexa/spotify200)

kaggle~ [my kaggle page for the dataset](https://www.kaggle.com/datasets/younver/spotify-top-200-dataset)
