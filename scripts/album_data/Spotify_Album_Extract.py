import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import requests
import pandas as pd
from pprint import pprint
import time
import xlwt

#### Adding client ID and secret to environmental variables ####
os.environ['SPOTIPY_CLIENT_ID'] = "7151208eaf8e4916864b5034a2ff9366"

os.environ['SPOTIPY_CLIENT_SECRET'] = '2babfb37534e415aa32d10bb77eedbdb'


#### Input Spotify URIs to query album data ####


def Get_Album_Info(album_uris):
    '''

    :param album_uris: list of uris pertaining to the musical albums. These URIs can be found using the Spotify app (R click on album -> share -> copy uri)
    :return: A pandas dataframe containing data on musical albums that won Tony awards.
    '''

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    uri = []
    name = []
    pop = []
    release_date = []
    markets = []
    track_uris = []

    for i in album_uris:
        album_info = sp.album(i)
        uri.append(album_info['uri'])
        name.append(album_info['name'])
        pop.append(album_info['popularity'])
        release_date.append(album_info['release_date'])
        markets.append(album_info['available_markets'])
        for track in album_info['tracks']['items']:
            track_uris.append(track['uri'])

#### Creating pandas dataframe with information about fields desired ####
    prelim_album_dataset = pd.DataFrame({'uri': [uri], 'Name': [name], 'Popularity': [pop],'Release Date': [release_date], 'Available Markets': [markets], 'Tracks': [track_uris]})
    return prelim_album_dataset



def Get_Track_Info(track_uris):
    '''

    :param track_uris: Using the list of tracks uploaded from the album, find feature metrics on those tracks
    :return: pandas dataframe with feature metrics for each track mentioned
    '''

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    id = []
    name = []
    artists = []
    popularity = []
    duration_ms = []
    for i in track_uris:
        track_info = sp.track(i)
        id.append(track_info['id'])
        name.append(track_info['name'])
        artists.append(track_info['artists'][0])
        popularity.append(track_info['popularity'])
        duration_ms.append(track_info['duration_ms'])

    prelim_track_dataset = pd.DataFrame(
        {'id': id, 'Name': name, 'Popularity': popularity, 'Artists': artists[0]['name'],
         'Duration MS': duration_ms})
    return prelim_track_dataset


def Get_Track_Analytics(track_uris):
    '''

    :param track_uris: Using the list of tracks uploaded from the album, find feature metrics on those tracks
    :return: pandas dataframe with feature metrics for each track mentioned
    '''

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    id = []
    key = []
    mode = []
    acousticness = []
    danceability = []
    energy = []
    instrumentalness = []
    liveness = []
    loudness = []
    speechiness = []
    tempo = []
    time_signature = []
    valence =[]
    for i in track_uris:
        track_info = sp.audio_features(i)
        id.append(track_info[0]['id'])
        key.append(track_info[0]['key'])
        mode.append(track_info[0]['mode'])
        acousticness.append(track_info[0]['acousticness'])
        danceability.append(track_info[0]['danceability'])
        energy.append(track_info[0]['energy'])
        instrumentalness.append(track_info[0]['instrumentalness'])
        liveness.append(track_info[0]['liveness'])
        loudness.append(track_info[0]['loudness'])
        speechiness.append(track_info[0]['speechiness'])
        tempo.append(track_info[0]['tempo'])
        time_signature.append(track_info[0]['time_signature'])
        valence.append(track_info[0]['valence'])


    prelim_track_dataset = pd.DataFrame(
        {'id': id,
         'Key': key,
         'Mode': mode,
         'Acoustics': acousticness,
         'Danceability': danceability,
         'Energy': energy,
         'Instrumentalness':instrumentalness,
         'Liveness':liveness,
         'Loudness':loudness,
         'Speechiness':speechiness,
         'Tempo':tempo,
         'Time Signature':time_signature,
         'Valence':valence
         })
    return prelim_track_dataset



def main():
    start_time = time.time()
    album_list = [
'spotify:album:2WQ4A0NReQExTbR70sFLtN',
'spotify:album:3T89YmayewCtYwhNscB6R0',
'spotify:album:583SgyGBxtEzsk9J8zBqiy',
'spotify:album:18DzAOVbSrw9RjOk3oTnzj',
'spotify:album:38kIjLnaTwbTHkiAQcSm5G',
'spotify:album:2QrINaaKpAWNtQfjzNaP5y',
'spotify:album:7N3G5LnFCtpF0A4Sdt6n8F',
'spotify:album:0VYMjNRDES7DPGkBQh8abf',
'spotify:album:5lQ3Ub1Uez0Qelrk5GTup0',
'spotify:album:0dTZmPIYidWSINfyQlm94q',
'spotify:album:5cK2RlgT7gseIqgxi9ITKb',
'spotify:album:5To3LrXgZuZEfDTiIjKqFf',
'spotify:album:4VYJtAzNUWPZfAGLh9iEcm',
'spotify:album:2GKE26bq2o8qoukpNlZnrh',
'spotify:album:1kCHru7uhxBUdzkm4gzRQc',
'spotify:album:0LhDyJXelg31FKLW5GDcKi',
'spotify:album:2RLYvCLS2sE77j6Vl8FVfc',
'spotify:album:1J1yxODbNlqKbwRqJxYJUP'
    ]
    spotify_album_data = Get_Album_Info(album_list)
    track_uris = spotify_album_data.iloc[:, 5][0]
    track_data = Get_Track_Info(track_uris)
    track_analytics = Get_Track_Analytics(track_uris)


    #Now, convert these to Excel spreadsheets#
    spotify_album_data.to_excel("../../Musical_Album_Info_Spotify.xls")
    track_data.to_excel("../../Musical_Track_Info_Spotify.xls")
    track_analytics.to_excel("../../Musical_Track_Analytical_Metrics_Spotify.xls")

    print("Returning information on these albums took", time.time() - start_time, " seconds to run.")


if __name__ == '__main__':
    main()