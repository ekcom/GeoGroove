import requests
import json


SPOTIFY_API_URL = "https://api.spotify.com/v1"

# Gets the user's ID
async def get_user_id(*, token: str):
    res = requests.get(f"{SPOTIFY_API_URL}/me", headers={ "Authorization": f"Bearer {token}" })
    print(f"get_user_id:\tSP API requet status {res.status_code}")
    json_data = res.json()
    return json_data["id"]

# Creates a private playlist
# and adds the listed tracks
async def create_playlist_with_tracks(name: str, tracks: list[str], *, user_id: str, token: str):
    playlist_id = await create_playlist(name, user_id=user_id, token=token)
    return await add_tracks_to_playlist(playlist_id, tracks, user_id=user_id, token=token)

# Creates a playlist
# and returns its id
async def create_playlist(name: str, *, user_id: str, token: str):
    json_to_send = {
        "name": name,
        "description": "Made with GeoGroove",
        "public": False
    }
    res = requests.post(f"{SPOTIFY_API_URL}/users/{user_id}/playlists",
                        headers={ "Authorization": f"Bearer {token}"},
                        data=json.dumps(json_to_send))
    print(f"create_playlist:\tSP API requet status {res.status_code}")
    json_data = res.json()
    return json_data["id"]

# Adds tracks to an existing playlist
async def add_tracks_to_playlist(playlist_id: str, tracks: list[str], *, user_id: str, token: str):
    res = requests.post(f"{SPOTIFY_API_URL}/playlists/{playlist_id}/tracks",
                        headers={ "Authorization": f"Bearer {token}" , "Content-Type": "application/json"},
                        data=json.dumps({ "uris": tracks, "position": 0 }))
    print(f"add_tracks_to_playlist:\tSP API requet status {res.status_code}")
    json_data = res.json()
    # todo return something meaningful
    #return json_data["?""]
    return True

async def get_tracks_for_artists(artist_names: list[str], *, token):
    tracks = []
    for artist_name in artist_names:
        artist_id = await get_artist_id(artist_name, token=token)
        artist_tracks = await get_top_track(artist_id, token=token)
        if artist_tracks:
            tracks += artist_tracks
    return tracks

async def get_artist_id(artist_name: str, *, token: str):
    res = requests.get(f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1", headers={ "Authorization": f"Bearer {token}" })
    print(f"get_artist_id:\tSP API requet status {res.status_code}")
    json = res.json()
    return json["artists"]["items"][0]["id"] if json["artists"]["items"] else None

async def get_top_track(artist_id: str, *, token: str):
    res = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks", headers={ "Authorization": f"Bearer {token}" })
    print(f"get_top_track:\tSP API requet status {res.status_code}")
    json = res.json()
    return [track["id"] for track in json["tracks"]] if json["tracks"] else None
