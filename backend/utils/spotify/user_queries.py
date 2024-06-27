import requests

# Gets the user's ID
async def get_user_id(*, token: str):
    res = requests.get("https://api.spotify.com/v1/me", headers={ "Authorization": f"Bearer {token}" })
    print(f"get_user_id:\tSP API requet status {res.status_code}")
    json = res.json()
    return json["id"]
