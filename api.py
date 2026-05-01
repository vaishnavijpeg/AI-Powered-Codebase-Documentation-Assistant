from fastapi import APIRouter
from app.services.repo_service import clone_repo
from app.utils.file_loader import load_files
from app.services.embedding_service import create_embedding
from app.services.retrieval_service import add_document

router = APIRouter()

@router.post("/ingest")

def ingest_repo(repo_url: str):

    repo_path = clone_repo(repo_url)

    files = load_files(repo_path)

    for file in files:

        embedding = create_embedding(file["content"])

        add_document(embedding,file["content"])

    return {"message":"Repository indexed successfully"}
