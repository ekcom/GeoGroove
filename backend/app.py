from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "test"}

app.mount("/", StaticFiles(directory="dist", html = True), name="dist")
