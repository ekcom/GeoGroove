from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from routers import auth


if __name__ == "__main__":
    print("Run this with `fastapi run app.py`")

load_dotenv()


app = FastAPI(docs_url=None)

app.include_router(auth.router)

@app.get("/test")
async def test():
    return {"message": "test"}

app.mount("/", StaticFiles(directory="dist", html = True), name="dist")
