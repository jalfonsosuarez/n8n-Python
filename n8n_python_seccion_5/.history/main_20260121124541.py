from fastapi import FastAPI, File, UploadFile


app = FastAPI(title="Image to WebP converter")

@app.get("/test")
def healt_check():
    return {"status": "ok", "message": "Convertidor app funcionando"}

@app.post("/convert-webp")
async def convert_webp(
    file: UploadFile = File(...),
    quality: int = 80
):
    pass