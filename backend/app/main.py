from fastapi import FastAPI
from app.api.routes.health import router as health_router

app = FastAPI(title="Veridoc Global API - Foundation")

app.include_router(health_router, prefix="/health")


@app.get("/")
def root():
    return {"message": "Veridoc Global Backend Running"}
