from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from routers import auth
from routers import forms
from routers import test


if __name__ == "__main__":
    print("Run this with `fastapi run app.py`")

load_dotenv()


app = FastAPI(docs_url=None)

# Routes
app.include_router(auth.router)
app.include_router(forms.router)
app.include_router(test.router)

app.mount("/", StaticFiles(directory="dist", html = True), name="dist")
