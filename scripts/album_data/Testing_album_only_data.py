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
    album_tracks = []
    track_uris = []
    tee = []
    for i in album_uris:
        album_info = sp.album(i)
        for t in album_info['tracks']['items']:
            name.append(album_info['name'])
            tee.append(t)
            p.append(album_info['popularity'])
    prelim_album_dataset = pd.DataFrame(
        {'Name': name, 'Tee':tee})
    print(prelim_album_dataset)
    return tee



Get_Album_Info(['spotify:album:2WQ4A0NReQExTbR70sFLtN','spotify:album:3T89YmayewCtYwhNscB6R0'])