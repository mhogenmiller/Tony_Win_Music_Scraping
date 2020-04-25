import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import requests
import pandas as pd
from pprint import pprint

#### Adding client ID and secret to environmental variables ####
os.environ['SPOTIPY_CLIENT_ID'] = "7151208eaf8e4916864b5034a2ff9366"

os.environ['SPOTIPY_CLIENT_SECRET'] = '2babfb37534e415aa32d10bb77eedbdb'


#### Input Spotify URIs to query album data ####

uri_list = ['spotify:album:1J1yxODbNlqKbwRqJxYJUP', 'spotify:album:1J1yxODbNlqKbwRqJxYJUP']

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

uri = []
name = []
pop = []
release_date = []
markets = []

for i in uri_list:
    album_info= sp.album(i)
    uri.append(album_info['uri'])
    name.append(album_info['name'])
    pop.append(album_info['popularity'])
    release_date.append(album_info['release_date'])
    markets.append(album_info['available_markets'])


#### Creating pandas dataframe with information about fields desired ####
prelim_album_dataset = pd.DataFrame({'uri': [uri], 'Name': [name], 'Popularity': [pop],'Release Date': [release_date], 'Available Markets': [markets]})
print(prelim_album_dataset)



