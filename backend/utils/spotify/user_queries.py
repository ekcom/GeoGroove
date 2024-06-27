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
    print(playlist_id)
    # TODO
    return True

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
