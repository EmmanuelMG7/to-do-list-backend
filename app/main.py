from fastapi import FastAPI

app = FastAPI(title="To-Do List API")

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}
