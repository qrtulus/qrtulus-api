from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "QRtulus API yayında reis!"}

@app.get("/shazam")
def detect_song():
    return JSONResponse(content={"status": "Shazam logic buraya gelecek"}, status_code=200)
