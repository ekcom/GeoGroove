from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse, FileResponse, JSONResponse
import spotipy
import os

from utils.get_playlist_name import gen_playlist_name


router = APIRouter(
    tags=["auth"],
)

@router.get("/auth/spotify")
def auth_sp():
    STATE = "TODO" # match with cookies or something

    #sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(os.environ["CLIENT_ID"], os.environ["CLIENT_SECRET"], redirect_uri="http://localhost:8000/callback", scope="playlist-modify-private"))
    return RedirectResponse(url=f"https://accounts.spotify.com/authorize?client_id={os.environ['CLIENT_ID']}&response_type=token&redirect_uri={os.environ['ORIGIN_URL']}/callback&state={STATE}&scope=playlist-modify-private user-top-read")

# Callback after Spotify auth
# hit on success or failure
@router.get("/callback")
def client_landed_page():
    # path is rel from `app.py`
    # todo use `os` or something to be sure
    return FileResponse("./dist/post-auth-sp.html")

@router.post("/make-playlist/spotify")
async def make_playlist_sp(request: Request):
    json = await request.json()
    print(json)
    user_id = "TODO get from params or something"
    spotify_track_list = [] # todo get list of tracks to import
    #playlist = sp.user_playlist_create(user_id, gen_playlist_name(), public=False, description="playlist description")
    #sp.user_playlist_add_tracks(user_id, playlist["id"], spotify_track_list)

    return JSONResponse({ "status": "error" })
