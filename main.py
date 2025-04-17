import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# RapidAPI Key
RAPIDAPI_KEY = "80732d43ddmshfb112014b927f53p12149fjsnfc08ae552a51"

# Headers
HEADERS_SHAZAM = {
    "x-rapidapi-host": "shazam.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY
}

HEADERS_YTMP3 = {
    "x-rapidapi-host": "youtube-mp36.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY
}

@app.get("/")
def root():
    return {"message": "QRtulus API aktif reis!"}

@app.get("/shazam")
def detect_song():
    # Shazam API'den örnek şarkı çekiyoruz (simülasyon)
    response = requests.get(
        "https://shazam.p.rapidapi.com/songs/list-recommendations",
        headers=HEADERS_SHAZAM,
        params={"key": "484129036", "locale": "en-US"}
    )

    if response.status_code != 200:
        return JSONResponse(status_code=500, content={"error": "Shazam API hatası"})

    data = response.json()
    track = data['tracks'][0]
    title = f"{track['subtitle']} - {track['title']}"

    # YouTube arama terimi oluştur
    search_query = title.replace(" ", "+")

    # YouTube search linkinden video ID çıkarılamadığı için şimdilik sabit video ID kullanıyoruz (test için)
    # Normalde YouTube API veya scraping ile video ID çekilebilir
    video_id = "4NRXx6U8ABQ"  # Blinding Lights örneği

    # RapidAPI'den reklamsız mp3 linki çek
    mp3_response = requests.get(
        f"https://youtube-mp36.p.rapidapi.com/dl?id={video_id}",
        headers=HEADERS_YTMP3
    )

    if mp3_response.status_code != 200:
        return JSONResponse(status_code=500, content={"error": "MP3 API hatası"})

    mp3_data = mp3_response.json()

    return JSONResponse(content={
        "title": title,
        "youtube_link": f"https://www.youtube.com/watch?v={video_id}",
        "mp3_download": mp3_data.get("link", "Link bulunamadı")
    })
