import pandas as pd
import requests
import base64
import random

all_df = pd.read_csv('./data/artist_cities_all.csv')


client_id = '49db8d61aa5d4982a6ec403ae0bc25d5'
client_secret = 'a629019030874cd4b2e1ed7f46a3f261'

auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()
auth_url = 'https://accounts.spotify.com/api/token'
auth_headers = {
    'Authorization': f'Basic {b64_auth_str}',
}
auth_data = {
    'grant_type': 'client_credentials',
}
auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_response.json()['access_token']

def get_artists(city, num_artists):
    artist_df = all_df[all_df['city'] == city]
    artist_list_full = artist_df['artist'].to_list()
    select_num = len(artist_list_full) // 10 + 10
    if (select_num > len(artist_list_full)):
        select_num = len(artist_list_full)
    if (select_num > 100):
        select_num = 100
    artist_list = random.sample(artist_list_full, select_num)

    def get_artist_popularity(artist_name):
        search_url = 'https://api.spotify.com/v1/search'
        search_headers = {
            'Authorization': f'Bearer {access_token}',
        }
        search_params = {
            'q': artist_name,
            'type': 'artist',
            'limit': 1,
        }
        search_response = requests.get(search_url, headers=search_headers, params=search_params)
        search_results = search_response.json()
        if search_results['artists']['items']:
            artist = search_results['artists']['items'][0]
            if artist['name'] != artist_name:
                return 0
            return artist['popularity']
        else:
            return 0

    popularities = []
    for artist_name in artist_list:
        popularities.append(get_artist_popularity(artist_name))

    sorted_artists, _ = zip(*sorted(list(zip(artist_list, popularities)), key=lambda x: x[1], reverse=True))
    sorted_artists = list(sorted_artists)[:min(len(sorted_artists), num_artists)]
    return sorted_artists

