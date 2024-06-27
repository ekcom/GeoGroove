import pandas as pd
import requests
import base64
import random

all_df = pd.read_csv('artist_cities_all.csv')


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

def get_artists(cities, playlist_len):
    num_artists = int((playlist_len/len(cities))/2)
    tot_artists = []

    for city in cities:
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
        for artist in sorted_artists:
            tot_artists.append(artist)

    return tot_artists

artist_list = get_artists(["Nashville", "San Francisco", "Phoenix"], 12)
print(artist_list)

def get_track_ids(artist_list, playlist_len):
    num_each = int(playlist_len/len(artist_list))
    print("# tracks per artist: ", num_each)
    track_ids = []
    for artist in artist_list:
        artist_id = None
        search_url = 'https://api.spotify.com/v1/search'
        search_headers = {
            'Authorization': f'Bearer {access_token}',
        }
        search_params = {
            'q': artist,
            'type': 'artist',
            'limit': 1,
        }
        search_response = requests.get(search_url, headers=search_headers, params=search_params)
        search_results = search_response.json()
        if search_results['artists']['items']:
            artist = search_results['artists']['items'][0]
            artist_id = artist['id']
            # print(artist_id)

        top_tracks_url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
        params = {
            'country': 'US'
        }
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        top_tracks_response = requests.get(top_tracks_url, headers=headers, params=params)
        if top_tracks_response.status_code == 200:
            top_tracks_data = top_tracks_response.json()
            for i in range(num_each):
                print(top_tracks_data['tracks'][i]['name'])
                track_ids.append(top_tracks_data['tracks'][i]['id'])

    return track_ids

get_track_ids(artist_list, 12)