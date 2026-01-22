from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="n8n + Python")

class IncomingData(BaseModel):
    text: str
    source: str | None = None
    

@app.post("analyze")
def analyze(data: IncomingData):
    return {"received_text": data.text, "lenght": len(data.text)}

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API funcionando OK :-)" }
