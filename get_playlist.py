import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
scope = 'playlist-modify-private playlist-modify-public'  # Ensure you have both scopes

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
artist_names = ['Dua Lipa', 'Ariana Grande', 'Billie Eilish', 'bentobox1995']
spotify_track_list = []

for artist_name in artist_names:
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    if results['artists']['items']:
        artist_id = results['artists']['items'][0]['id']
        top_tracks = sp.artist_top_tracks(artist_id)
        spotify_track_list.extend([track['uri'] for track in top_tracks['tracks']])

# Assuming we need user_id for some operation, get it from Spotify
user_id = sp.current_user()['id']

# Send POST request to the Express server
response = requests.post(f'http://localhost:8000/create_playlist', json={
    'access_token': sp.auth_manager.get_access_token()['access_token'],
    'tracks': spotify_track_list
})

if response.status_code == 200:
    print('Playlist created and tracks added successfully')
    print('Playlist URL:', response.json()['playlist_url'])
else:
    print('Failed to create playlist or add tracks:', response.text)
