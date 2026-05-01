import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_answer(question, context):

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
