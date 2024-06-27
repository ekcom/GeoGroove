from fastapi import APIRouter
from starlette.responses import RedirectResponse, FileResponse
import spotipy
import os

from utils.get_playlist_name import gen_playlist_name


router = APIRouter(
    tags=["auth"],
)

@router.get("/auth/spotify")
async def auth_sp():
    STATE = "TODO" # match with cookies or something

    #sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(os.environ["CLIENT_ID"], os.environ["CLIENT_SECRET"], redirect_uri="http://localhost:8000/callback", scope="playlist-modify-private"))
    return RedirectResponse(url=f"https://accounts.spotify.com/authorize?client_id={os.environ['CLIENT_ID']}&response_type=token&redirect_uri={os.environ['ORIGIN_URL']}/callback&state={STATE}&scope=playlist-modify-private user-top-read")

# Callback after Spotify auth
# hit on success or failure
@router.get("/callback")
def client_landed_page():
    return FileResponse("./dist/post-auth-sp.html")
