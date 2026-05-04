# AI-Powered Codebase Documentation Assistant
An AI-powered backend system that enables developers to **query and understand large codebases using natural language**.  
The system ingests repositories, generates embeddings for source code and documentation, performs **semantic search using FAISS**, and uses an **LLM to generate contextual answers**.

This project demonstrates how modern AI systems combine **Retrieval-Augmented Generation (RAG), vector search, and backend APIs** to build intelligent developer tools.

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


# Features

### Repository Ingestion
- Clone any GitHub repository
- Extract relevant files such as `.py`, `.js`, `.ts`, `.md`, `.txt`
- Convert files into embeddings

### Semantic Code Search
- Uses **vector embeddings** to understand semantic meaning
- Stores embeddings using **FAISS vector index**
- Retrieves the most relevant code snippets

### LLM-Powered Answers
- Combines retrieved context with user queries
- Generates detailed explanations using an LLM API

### FastAPI Backend
- Scalable REST APIs
- Clean modular architecture
- Designed for production-ready systems

### Extensible Architecture
The system can be extended with:
- GitHub webhooks
- PR review assistants
- automatic documentation generation
- multi-repo support


