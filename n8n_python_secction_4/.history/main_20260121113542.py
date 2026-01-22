import re
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="n8n + Python")

class IncomingData(BaseModel):
    text: str
    source: str | None = None
    
SPANISH_STOPWORDS = {
    "de", "la", "que", "el", "en", "y", "a", "los", "del", "se", "las",
    "por", "un", "para", "con", "no", "una", "su", "al", "lo", "como",
    "más", "mas", "o", "pero", "sus", "le", "ya", "si", "porque", "cuando",
    "muy", "sin", "sobre", "también", "tambien", "me", "hasta", "hay",
    "donde", "han", "quien", "entre", "está", "esta", "ser", "son",
}


def tokenize(text: str) -> List[str]:
    text = text.lower()
    return re.findall(r"[a-záéíóúüñ]+", text, flags=re.IGNORECASE)
    

@app.post("/analyze")
def analyze(data: IncomingData):
    text = data.text.strip()
    words = [word for word in text.split()]
    word_count = len(words)
    return {"received_text": data.text, "lenght": len(data.text), "words": words, "words_count": word_count}

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API funcionando OK :-)" }
