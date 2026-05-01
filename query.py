from fastapi import APIRouter
from app.schemas.query_schema import QueryRequest
from app.services.embedding_service import create_embedding
from app.services.retrieval_service import search
from app.services.llm_service import generate_answer

router = APIRouter()

@router.post("/query")

def query_codebase(request: QueryRequest):

    query_embedding = create_embedding(request.question)

    docs = search(query_embedding)

    context = "\n".join(docs)

    answer = generate_answer(request.question, context)

    return {"answer":answer}
