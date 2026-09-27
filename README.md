# OpsMind

> AI-Powered Engineering Knowledge & Operations Assistant

OpsMind is a GenAI project designed to help
software engineering and operations teams interact with their
technical knowledge, documentation, incidents, and operational data.

The project is being built incrementally to explore and implement
modern GenAI application architecture.

## Current Status

🚧 Work in Progress

Currently implemented:

- FastAPI backend
- Local LLM integration using Ollama
- Async LLM communication
- Configuration management
- Basic health endpoint
- Basic chat endpoint

Upcoming:

- [ ] Document ingestion
- [ ] Document chunking
- [ ] Local embeddings
- [ ] PostgreSQL + pgvector
- [ ] Semantic retrieval
- [ ] RAG pipeline
- [ ] Source citations
- [ ] RAG evaluation
- [ ] Tool calling
- [ ] Agentic workflows
- [ ] Observability
- [ ] Docker deployment


---

## Architecture

Current architecture:

```text
Client
  |
  v
FastAPI
  |
  v
ChatService
  |
  v
LLMClient
  |
  v
Ollama
  |
  v
Local LLM
