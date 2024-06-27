from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse, FileResponse, JSONResponse
import os
import json

from utils.get_playlist_name import gen_playlist_name
from utils.spotify.user_queries import get_user_id, create_playlist_with_tracks, get_tracks_for_artists


router = APIRouter(
    tags=["auth"],
)

@router.get("/auth/spotify")
def auth_sp():
    STATE = "TODO" # match with cookies or something

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
    json_req = await request.json() # { token, state }
    user_id = await get_user_id(token=json_req["token"])
    artists_raw = request.cookies.get("artists")
    print(f"artists_raw: {artists_raw}") # TODO
    if artists_raw == None:
        return JSONResponse({ "status": "error" })
    #artists = json.loads(artists_raw)
    artists = artists_raw.split(",")
    print(f"/make-playlist-spotify\tGetting tracks for {artists}")
    spotify_track_list = await get_tracks_for_artists(artists, token=json_req["token"])
    ok = await create_playlist_with_tracks(gen_playlist_name(), spotify_track_list, user_id=user_id, token=json_req["token"])

    if ok:
        return JSONResponse({ "status": "ok" })
    return JSONResponse({ "status": "error" })
