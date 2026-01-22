from fastapi import FastAPI

app = FastAPI(title="n8n + Python")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API funcionando OK :-)" }
