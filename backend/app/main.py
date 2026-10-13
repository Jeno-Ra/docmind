from fastapi import FastAPI
app = FastAPI(title="PortfolioHub API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/works/{work_id}")
def get_work(work_id: int):
    return {"work_id": work_id}

@app.get("/works")
def list_works(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}