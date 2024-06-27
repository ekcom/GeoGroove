from fastapi import APIRouter, Request, Response
from starlette.responses import JSONResponse
import json

from utils.data.artists_from_city import get_artists, get_track_ids

router = APIRouter()

@router.post("/submit-form")
async def form(request: Request, response: Response):
    req_json = await request.json() # []
    locations_list = req_json["locations"]

    artists = get_artists(locations_list, 12)

    #response.set_cookie(key="chocolate-chip", value="".join(random.choices("0123456789", k=10)))
    response.set_cookie(key="artists", value=json.dumps(artists)) # not working :(

    return JSONResponse({ "status": "ok", "artists": artists })

@router.get("/asd")
async def form(request: Request, response: Response):
    ct = request.cookies.get("ct")
    ct += 2
    response.set_cookie(key="ct", value=ct)
    return { "ct": ct }
