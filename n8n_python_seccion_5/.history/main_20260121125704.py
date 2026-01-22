import io
from fastapi import FastAPI, File, UploadFile
from PIL import Image

app = FastAPI(title="Image to WebP converter")

@app.get("/test")
def healt_check():
    return {"status": "ok", "message": "Convertidor app funcionando"}

@app.post("/convert-webp")
async def convert_webp(
    file: UploadFile = File(...),
    quality: int = 80
):
    original_bytes = await file.read()
    image = Image.open(io.BytesIO(original_bytes))
    
    if image.mode in ("P", "LA"):
        image = image.convert("RGBA")
    elif image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")
        
    output_buffer = io.BytesIO()
    
    image.save(
        output_buffer,
        format="WEBP",
        quality=quality,
        method=6,
    )
    
    output_buffer.seek(0)
    
    return Response(
        content = output_buffer.read(),
        media_type = "image/webp"
    )