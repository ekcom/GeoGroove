import requests

# Gets the user's ID
async def get_user_id(*, token: str):
    res = requests.get("https://api.spotify.com/v1/me", headers={ "Authorization": f"Bearer {token}" })
    print(f"get_user_id:\tSP API requet status {res.status_code}")
    json = res.json()
    return json["id"]
async def get_artist_id(*, artist_Name: str, token: str):
    res = requests.get(f"https://api.spotify.com/v1/search?q={artist_Name}&type=artist&limit=1", headers={ "Authorization": f"Bearer {token}" })
    print(f"get_artist_id:\tSP API requet status {res.status_code}")
    json = res.json()
    return json["artists"]["items"][0]["id"] if json["artists"]["items"] else None
async def get_top_track(*, artist_id: str, token: str):
    res = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks", headers={ "Authorization": f"Bearer {token}" })
    print(f"get_top_track:\tSP API requet status {res.status_code}")
    json = res.json()
    return [track["id"] for track in json["tracks"]] if json["tracks"] else None

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))
# artist_names = ['Dua Lipa', 'Ariana Grande', 'Billie Eilish', 'bentobox1995']
# spotify_track_list = []
# for artist_name in artist_names:
#     results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
#     if results['artists']['items']:
#         artist_id = results['artists']['items'][0]['id']
#         print(f"Artist found: {artist_name} (ID: {artist_id})")
#         top_tracks = sp.artist_top_tracks(artist_id)
#         print(f"Top tracks for {artist_name}: top_tracks:{[track['id'] for track in top_tracks['tracks']]}")
#         spotify_track_list += [track['id'] for track in top_tracks['tracks']]
#     else:
#         print(f"No matching artist found for '{artist_name}'.")