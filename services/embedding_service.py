import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def create_embedding(text):

    response = openai.Embedding.create(
        input=text,
        model="text-embedding-3-small"
    )

    return response["data"][0]["embedding"]
