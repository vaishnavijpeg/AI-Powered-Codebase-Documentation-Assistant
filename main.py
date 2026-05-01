from fastapi import FastAPI
from app.api import ingest, query

app = FastAPI(title="AI Codebase Documentation Assistant")

app.include_router(ingest.router)
app.include_router(query.router)
