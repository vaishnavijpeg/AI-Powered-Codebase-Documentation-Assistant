# AI-Powered Codebase Documentation Assistant

A FastAPI backend that enables developers to ask natural language questions about any GitHub repository.

## Features

- Repository ingestion and indexing
- Semantic search using embeddings + FAISS
- LLM-based contextual answers
- FastAPI REST APIs
- PostgreSQL metadata storage
- Redis caching

## Tech Stack

- FastAPI
- PostgreSQL
- Redis
- FAISS
- OpenAI API
- Docker

## Run

pip install -r requirements.txt
uvicorn app.main:app --reload
