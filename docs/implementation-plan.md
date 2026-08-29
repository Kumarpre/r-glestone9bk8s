# Implementation Plan: Mutual Fund FAQ Assistant

This document outlines the phase-wise implementation strategy for the Mutual Fund FAQ Assistant, based on the requirements defined in the `problemStatement.md` and the system design in `Architecture.md`.

## Phase 1: Environment Setup & Project Scaffolding
**Goal**: Initialize the project structure, development environment, and install base dependencies.
- Create the project directory structure (`data/`, `src/`, `docs/`, `frontend/`, `tests/`).
- Set up a Python 3.11+ virtual environment.
- Install necessary backend dependencies (`fastapi`, `uvicorn`, `langchain` / `llama-index`, `chromadb`, `sentence-transformers`, `beautifulsoup4`, `google-genai`).
- Set up the `.env` file for OpenAI API keys, base URL, and configurations.

## Phase 2: Offline Data Pipeline (Ingestion)
**Goal**: Build the pipeline to fetch, process, and index the mutual fund scheme data from Groww.

### Phase 2.1: Source Identification & Acquisition
- Configure the document fetcher to download the 5 designated HDFC mutual fund scheme pages from `groww.in`.
- Save the raw HTML content locally into `data/raw/`.

### Phase 2.2: Parsing & Normalization
- Implement the HTML parser (`BeautifulSoup` or `trafilatura`) to extract plain text and structural data (expense ratio, exit load, riskometer, benchmark, etc.).
- Normalize the text, clean up unicode and whitespace, and save the output to `data/processed/`.

### Phase 2.3: Chunking & Indexing
- Define and apply a chunking strategy:
  - **Chunker**: Use LangChain's `RecursiveCharacterTextSplitter`.
  - **Separators**: Split on `\n\n`, then `\n`, then `" "` to respect the line-by-line nature of the parsed HTML.
  - **Chunk Size**: 600-800 characters.
  - **Overlap**: 100-150 characters to maintain context across split lines.
- Generate embeddings using a local open-source model (e.g., `bge-small-en` via `sentence-transformers`).
- Upsert the chunked documents along with rich metadata into a local ChromaDB vector store (`data/index/`).

## Phase 3: Core RAG Components (Retrieval)
**Goal**: Implement the online retrieval mechanism to fetch relevant chunks based on user queries.
- Develop the retriever module (`src/retrieval/retriever.py`):
  - **Strategy**: Metadata-Filtered Semantic Search.
  - **Metadata Pre-filtering (Crucial)**: Because chunks share identical vocabulary (e.g., "Expense ratio", "Exit load") across all 5 schemes, the retriever *must* extract the target scheme from the user's query and apply a hard ChromaDB metadata filter (`where={"scheme_id": "..."}`) before vector search.
  - **Top-K Retrieval**: Fetch the top `k=4` chunks. The slightly higher `k` accounts for the noise in the BeautifulSoup-extracted HTML text.
  - **Distance Thresholding**: Implement a similarity score cutoff to reject chunks that are too semantically distant (preventing hallucination for out-of-scope questions).

## Phase 4: LLM Generation & Query Classifier (OpenAI-Compatible API)
**Goal**: Integrate an OpenAI-compatible API for query classification and factual response generation.
- **Query Classifier**: Implement a hybrid intent classifier (Rule-based + `qwen/qwen3-32b` fallback) to detect whether a query is Factual, Advisory, Comparative, or Out-of-Scope.
- **Generator**: Utilize `openai/gpt-oss-120b` to generate responses.
- Implement strict prompting to enforce context-only generation and prevent hallucinations or investment advice.

## Phase 5: Response Validation & Guardrails
**Goal**: Enforce strict constraints on the final output to ensure compliance.
- Build the `Response Validator` to guarantee that all factual answers:
  - Are strictly limited to a maximum of 3 sentences.
  - Contain exactly 1 valid citation URL matching the allowlist (`groww.in`).
  - Include the required footer: `"Last updated from sources: <date>"`.
- **Refusal Handler**: Return polite, templated refusals for advisory/comparative queries with an educational link (`https://groww.in/p/mutual-funds`).
- **Rate Limit Handling**: Implement exponential backoff for API rate limits (respecting TPM and RPM limits).

## Phase 6: API & User Interface
**Goal**: Expose the backend logic through an API and build a minimal frontend.

### Phase 6.1: API Development
- Develop FastAPI routes:
  - `GET /health` for liveness checks.
  - `POST /chat` to handle incoming user queries and orchestrate the Classifier -> Retriever -> Generator -> Validator pipeline.

### Phase 6.2: Frontend Development
- Build a minimal, responsive web UI (using React, Next.js, or Vite).
- Implement a chat interface featuring:
  - A persistent disclaimer: "Facts-only. No investment advice."
  - 3 pre-filled example queries.
  - Display of citation links and footer in assistant responses.

## Phase 7: Automation & Scheduler
**Goal**: Automate the data ingestion pipeline to keep information up-to-date.
- Configure a GitHub Actions workflow to act as a scheduler.
- The scheduler must run daily at **10:00 AM IST**.
- Trigger the full ingestion script (scraping, normalization, chunking, embedding, and updating ChromaDB) on each run to ensure the offline corpus is fresh.

**Status**: Implemented via `.github/workflows/scheduler.yml` which triggers `scripts/ingest_all.py` every day at 10:00 AM IST (04:30 AM UTC).
