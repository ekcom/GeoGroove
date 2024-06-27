from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(docs_url=None)

@app.get("/test")
async def test():
    return {"message": "test"}

app.mount("/", StaticFiles(directory="dist", html = True), name="dist")
