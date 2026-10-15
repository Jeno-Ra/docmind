from fastapi import FastAPI, HTTPException
from backend.app.schemas import WorkCreate,WorkResponse
app = FastAPI(title="PortfolioHub API", version="0.1.0")

#内版本储存：进程重启就清空
_work:list[dict] = []
_next_id:int = 1
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/works",response_model=WorkResponse,status_code=201)
def create_work(work: WorkCreate):
    global _next_id
    record = {"id": _next_id, **work.model_dump()}
    _work.append(record)
    _next_id += 1
    return record

@app.get("/works",response_model=list[WorkResponse])
def list_works(skip: int = 0, limit: int = 10):
    return _work[skip : skip + limit]

@app.get("/works/{work_id}",response_model=WorkResponse)
def get_work(work_id: int):
    for w in _work:
        if w["id"] == work_id:
            return w
    raise HTTPException(status_code=404, detail="作品不存在")