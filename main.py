from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "QRtulus API yayında reis!"}

@app.get("/shazam")
def detect_song():
    return {
        "title": "The Weeknd - Blinding Lights",
        "youtube_link": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
        "mp3_download": "https://yt-download.org/api/widget/mp3/4NRXx6U8ABQ"
    }
