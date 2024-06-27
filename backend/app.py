from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

if __name__ == "__main__":
    print("Run this with `fastapi run app.py`")

load_dotenv()

app = FastAPI(docs_url=None)

@app.get("/test")
async def test():
    return {"message": "test"}

app.mount("/", StaticFiles(directory="dist", html = True), name="dist")
