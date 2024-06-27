from fastapi import APIRouter

from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth


router = APIRouter(
    tags=["auth"],
)

@router.get("/auth/spotify")
async def auth_sp():
    user_id = "TODO get from params or something"
    spotify_track_list = [] # todo get list of tracks to import

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(os.environ["CLIENT_ID"], os.environ["CLIENT_SECRET"], redirect_uri="http://localhost:8000/callback", scope="playlist-modify-private"))
    playlist = sp.user_playlist_create(user_id, "playlist name", public=False, description="playlist description")
    sp.user_playlist_add_tracks(user_id, playlist["id"], spotify_track_list)

    # TODO return a redirect or something

# Callback after Spotify auth
# hit on success or failure
@router.get("/callback")
    # todo
