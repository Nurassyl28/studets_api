
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.students import router as students_router

app = FastAPI(title="Student Directory API", version="1.0.0")

origins = []
raw_origins = os.getenv("CORS_ORIGINS", "")
if raw_origins:
    origins = [o.strip() for o in raw_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(students_router, prefix="/api", tags=["students"])

@app.get("/health")
def health():
    return {"status": "ok"}
