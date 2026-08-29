# Problem Statement: Mutual Fund FAQ Assistant (Facts-Only Q&A)

## Overview
The objective of this project is to build a facts-only FAQ assistant for mutual fund schemes, using Groww as the reference product context. The assistant will answer objective, verifiable queries related to mutual funds by retrieving information exclusively from official public sources, such as AMC (Asset Management Company) websites, AMFI, and SEBI.

The system must strictly avoid providing investment advice, opinions, or recommendations. Every response must include a single, clear source link and adhere to defined constraints around clarity, accuracy, and compliance.

## Objective
Design and implement a lightweight Retrieval-Augmented Generation (RAG)-based assistant that:
- Answers factual queries about mutual fund schemes
- Uses a curated corpus of official documents
- Provides concise, source-backed responses

## Target Users
- Retail investors comparing mutual fund schemes
- Customer support and content teams handling repetitive mutual fund queries

## Scope of Work

### 1. Corpus Definition
- Select one Asset Management Company (AMC)
- Choose 3–5 mutual fund schemes, ensuring category diversity (e.g., large-cap, flexi-cap, ELSS)
  - https://groww.in/mutual-funds/hdfc-mid-cap-fund-direct-growth
  - https://groww.in/mutual-funds/hdfc-small-cap-fund-direct-growth
  - https://groww.in/mutual-funds/hdfc-gold-etf-fund-of-fund-direct-plan-growth
  - https://groww.in/mutual-funds/hdfc-large-cap-fund-direct-growth
  - https://groww.in/mutual-funds/hdfc-elss-tax-saver-fund-direct-plan-growth

### 2. FAQ Assistant Requirements
The assistant must:
- Answer facts-only queries, such as:
  - Expense ratio of a scheme
  - Exit load details
  - Minimum SIP amount
  - ELSS lock-in period
  - Riskometer classification
  - Benchmark index
  - Process to download statements or capital gains reports
- Ensure:
  - Each response is limited to a maximum of 3 sentences
  - Each response includes exactly one citation link
  - Each response includes a footer: “Last updated from sources: <date>”

### 3. Refusal Handling
The assistant must refuse non-factual or advisory queries, such as:
- “Should I invest in this fund?”
- “Which fund is better?”

Refusal responses should:
- Be polite and clearly worded
- Reinforce the facts-only limitation
- Provide a relevant educational link (e.g., AMFI or SEBI resource)

### 4. User Interface (Minimal)
The solution should include a simple interface with:
- A welcome message
- Three example questions
- A visible disclaimer: “Facts-only. No investment advice.”

## Constraints

### Data and Sources
- Use only official public sources (AMC, AMFI, SEBI)
- Do not use third-party blogs or aggregator websites

### Privacy and Security
- Do not collect, store, or process:
  - PAN or Aadhaar numbers
  - Account numbers
  - OTPs
  - Email addresses or phone numbers

### Content Restrictions
- No investment advice or recommendations
- No performance comparisons or return calculations
- For performance-related queries, provide a link to the official factsheet only

### Transparency
- Responses must be short, factual, and verifiable
- Every answer must include a source link and last updated date

## Expected Deliverables
- **README Document**
  - Setup instructions
  - Selected AMC and schemes
  - Architecture overview (RAG approach)
  - Known limitations
- **Disclaimer Snippet**
  - “Facts-only. No investment advice.”

## Success Criteria
- Accurate retrieval of factual mutual fund information
- Strict adherence to facts-only responses
- Consistent inclusion of valid source citations
- Proper refusal of advisory queries
- Clean, minimal, and user-friendly interface

## Summary
The goal is to build a trustworthy, transparent, and compliant mutual fund FAQ assistant that prioritizes accuracy over intelligence. The system should ensure that users receive only verified, source-backed financial information, without any advisory bias or speculative content.

---

# Context Setup
- problemStatement.txt
- problemStatement.md
- architecture.md
- implementation-plan.md
- egde-case.md

# Prompt
- Generate problemStatement.md to store entire context of this project using @docs/problemStatement.txt
- Generate a detailed Architecture.md for this @docs/problemStatement.md
- Generate a phase-wise implementation-plan.md using @docs/Architecture.md and @docs/problemStatement.md
- Groq as a LLM we will using in this project so update @docs/Architecture.md and @docs/implementation-plan.md
- Generate a edge-case.md using @docs/implementation-plan.md
- Generate an eval.md using the @docs/implementation-plan.md
- In the @docs/Architecture.md the Corpus & Source Model will be the URLs present from grow rather than different website
- Fix the @docs/Architecture.md and then update the @docs/implementation-plan.md
- Implement phase1 as per the @docs/implementation-plan.md
- Implement phase2.1 (Source identification & acquisition) as per the @docs/implementation-plan.md
- Implement phase2.2 (Parsing & normalization) as per the @docs/implementation-plan.md
- Using the @data/processed update the chunking strategy in the @docs/implementation-plan.md
- Implement phase2.3 as per the @docs/implementation-plan.md
- Understand the @data/processed see the chunks and find the best retrieval strategy and update in the @docs/implementation-plan.md
- Implement phase3 as per the @docs/implementation-plan.md
- Implement phase4 as per the @docs/implementation-plan.md
- Implement phase5 as per the @docs/implementation-plan.md
- llama-3.3-70b-versatile and llama-3.1-8b-instant are decommissioned so they cannot be used
- we can use these models openai/gpt-oss-120b
- Groq API call is failing after adding API key fix the issue
- openai/gpt-oss-120b
  - request per minute - 30
  - request per day - 1K
  - Tokens per minute - 8K
  - Tokens per day - 200K
  - In phase5 take care of these limits as well
- Implement phase6.1 (API) as per the @docs/implementation-plan.md
- Write a prompt for google stitch for phase6.2
- We will make good quality frontend design with google stitch
- Implement phase6.2 (Frontend) using stitch folder with react as per the implementation-plan.md
- Using @stitch_hdfc_fund_fact_assistant
- Implement phase6.2 frontend part using the @docs/implementation-plan.md
- we can make use of react, vite or nextjs to build the frontend part
- Unable to reach the server. Please try again.
- Backend I guess is not running properly above error is coming
- Run the project
- Stop the project
- In the @docs/implementation-plan.md update the phase7 with scheduler
- we want to make scheduler with github action
- this scheduler will run everyday and update the ingestion component so that daily we have the latest data
- so scrapping, normalization, chunking, embedding and updating the chromadb is done daily
- Implement phase7 scheduler phase using the @docs/implementation-plan.md
- scheduler will run everyday at 10:00AM IST
- Pushed the project on github
- VERIFIED the scheduler is running
- Deployment-plan.md
- Deploy the project on railway for backend
- Deploy the project on vercel for frontend

---

# Architecture: Mutual Fund FAQ Assistant
*Facts-only. No investment advice.*

This document describes the system architecture for a lightweight, compliance-first Retrieval-Augmented Generation (RAG) assistant that answers factual mutual fund queries by retrieving information from Groww scheme pages — the reference product context defined in the Problem Statement.

**Related documents:** Problem Statement

## Table of Contents
1. Design Principles
2. High-Level Architecture
3. Component Overview
4. Data Pipeline (Offline)
5. Query Pipeline (Online)
6. RAG Design
7. Query Classification & Refusal Handling
8. Response Contract
9. Corpus & Source Model
10. User Interface
11. Technology Stack
12. Project Structure
13. Security, Privacy & Compliance
14. Deployment Model
15. Observability & Quality
16. Known Limitations
17. Future Extensions (Out of Scope)

## 1. Design Principles
- **Accuracy over intelligence**: Prefer retrieved facts and templated responses over open-ended LLM reasoning
- **Source-backed only**: Every factual answer cites exactly one Groww scheme URL; no unsourced claims
- **Facts-only boundary**: Classify and refuse advisory, comparative, or speculative queries before retrieval
- **Minimal surface area**: No user accounts, no PII collection, no session persistence of sensitive data
- **Groww corpus only**: Corpus built exclusively from the 5 Groww mutual fund scheme pages listed in the problem statement
- **Deterministic guardrails**: Post-generation validation enforces sentence count, citation presence, and disclaimer footer

## 2. High-Level Architecture
The system splits into an offline ingestion path (corpus build) and an online query path (user Q&A). A thin web UI talks to a single backend API that orchestrates classification, retrieval, generation, and validation.

**Offline — Corpus Build**
- Document Fetcher -> Parser & Normalizer -> Chunker + Metadata -> Embedding Model -> Vector Store

**Online — Query Serving**
- Web UI -> API Gateway / Chat Endpoint -> Query Classifier
- For Factual: Retriever -> Groq Generator -> Response Validator
- For Advisory / Out of scope: Refusal Handler

### Request lifecycle (summary)
1. User submits a question via the UI.
2. Backend classifies intent (factual vs advisory vs out-of-scope).
3. For factual queries: retrieve top-k relevant chunks, generate a constrained answer, validate format.
4. For advisory queries: return a polite refusal with an educational link.
5. UI renders the response with citation and footer.

## 3. Component Overview
- **Document Fetcher**: Download Groww scheme pages (HTML) for each of the 5 HDFC funds (Offline)
- **Parser**: Extract text from Groww HTML; preserve key fund attributes (Offline)
- **Chunker**: Split documents into retrieval units with rich metadata (Offline)
- **Embedding Service**: Convert chunks to vectors (Offline + query time)
- **Vector Store**: Persist embeddings and metadata for similarity search (Both)
- **Query Classifier**: Detect advisory/comparative/performance-calculation intent (Online)
- **Retriever**: Hybrid or dense retrieval scoped by scheme/category (Online)
- **Generator**: Call Groq to produce ≤3-sentence answer grounded in retrieved context (Online)
- **Response Validator**: Enforce citation, sentence limit, footer, no advice language (Online)
- **Refusal Handler**: Return compliant refusal + Groww educational link (Online)
- **Web UI**: Chat input, example prompts, disclaimer, citation display (Online)

## 4. Data Pipeline (Offline)

### 4.1 Source acquisition
The corpus is built from one Groww scheme page per fund — the same URLs listed in Problem Statement §1. No AMC, AMFI, or SEBI sites are ingested separately.

- HDFC Mid Cap Fund Direct Growth (Mid-cap): https://groww.in/mutual-funds/hdfc-mid-cap-fund-direct-growth
- HDFC Small Cap Fund Direct Growth (Small-cap): https://groww.in/mutual-funds/hdfc-small-cap-fund-direct-growth
- HDFC Gold ETF Fund of Fund Direct Plan Growth (Gold / FoF): https://groww.in/mutual-funds/hdfc-gold-etf-fund-of-fund-direct-plan-growth
- HDFC Large Cap Fund Direct Growth (Large-cap): https://groww.in/mutual-funds/hdfc-large-cap-fund-direct-growth
- HDFC ELSS Tax Saver Fund Direct Plan Growth (ELSS): https://groww.in/mutual-funds/hdfc-elss-tax-saver-fund-direct-plan-growth

Each page is the single source of truth for that scheme. Facts such as expense ratio, exit load, minimum SIP, riskometer, benchmark, and lock-in (where shown) are extracted from the page content at ingest time.
*Refusal citations (not ingested)*: Advisory refusals link to the Groww mutual funds overview — https://groww.in/p/mutual-funds.

### 4.2 Ingestion flow
Trigger ingest for scheme -> Fetcher -> Save raw PDF/HTML -> Parser -> Extract plain text + structure -> Chunker -> Section-aware chunks -> Embedder -> Batch embed -> Vector DB -> Upsert with metadata.

### 4.3 Parsing strategy
- **Groww scheme pages (HTML)**: Fetch each scheme URL; extract main fund details. Use BeautifulSoup / trafilatura; if content is JS-rendered, use Playwright or similar for a one-time ingest snapshot.
- **Normalization**: Unicode cleanup, whitespace collapse, strip navigation chrome; retain labeled attribute blocks.
- **Date extraction**: Use page "Last updated" text if present; otherwise fall back to ingested_at.

### 4.4 Chunking strategy
- **Chunk size**: 400–800 tokens (Fits single facts without noise)
- **Overlap**: 50–100 tokens (Preserves context across section boundaries)
- **Split boundary**: Headings, tables, paragraphs (Keeps semantic units intact)

Required chunk metadata:
```json
{
  "scheme_id": "hdfc-elss-tax-saver-direct-growth",
  "scheme_name": "HDFC ELSS Tax Saver Fund Direct Plan Growth",
  "category": "ELSS",
  "amc": "HDFC Mutual Fund",
  "document_type": "groww_scheme_page",
  "source_url": "https://groww.in/mutual-funds/hdfc-elss-tax-saver-fund-direct-plan-growth",
  "source_domain": "groww.in",
  "page_or_section": "Scheme Information",
  "content_hash": "sha256:...",
  "document_date": "2025-07-31",
  "ingested_at": "2026-08-23T00:00:00Z"
}
```

### 4.5 Re-indexing policy
- Re-run ingestion when Groww scheme page content changes (spot-check monthly or on demand).
- Store document_date and surface the latest date in the response footer.
- Version chunks by content_hash; deduplicate on re-ingest.

## 5. Query Pipeline (Online)

### 5.1 API surface (minimal)
- `/health` (GET): Liveness check
- `/chat` (POST): Accept user message; return assistant response
- `/schemes` (GET): List indexed schemes (optional, for UI hints)

Example request:
```json
{
  "message": "What is the expense ratio of HDFC Large Cap Fund Direct Growth?"
}
```

Example factual response:
```json
{
  "type": "answer",
  "text": "The direct plan growth option of HDFC Large Cap Fund carries an expense ratio of 0.96% as per the Groww scheme page. This ratio represents the annual fee charged by the fund house for managing the scheme.",
  "citation": {
    "url": "https://groww.in/mutual-funds/hdfc-large-cap-fund-direct-growth",
    "title": "HDFC Large Cap Fund Direct Growth — Groww"
  },
  "footer": "Last updated from sources: 2025-07-31",
  "disclaimer": "Facts-only. No investment advice."
}
```

Example refusal response:
```json
{
  "type": "refusal",
  "text": "I can only answer factual questions about mutual fund schemes and cannot provide investment advice or recommendations. For general guidance on mutual funds, please refer to Groww's investor resources.",
  "citation": {
    "url": "https://groww.in/p/mutual-funds",
    "title": "Mutual Funds on Groww"
  },
  "footer": "Last updated from sources: 2026-08-23",
  "disclaimer": "Facts-only. No investment advice."
}
```

## 6. RAG Design

### 6.1 Retrieval
**Approach**: Dense vector retrieval with optional metadata filtering.
- Embed the user query with the same model used at ingest time.
- Filter by scheme_name or category if detected in the query (entity extraction or keyword match).
- Retrieve top k = 5 chunks; rerank to top 3 if a cross-encoder reranker is available (optional for v1).
- Pass retrieved chunks + metadata (especially source_url, document_date) to the generator.

**Fallback when retrieval confidence is low**:
- If max similarity score < threshold, respond: "I couldn't find verified information for that query in our sources" and link to the relevant Groww scheme page if the scheme is identified.

### 6.2 Generation
The generator calls Groq (`llama-3.3-70b-versatile` by default) under a strict system prompt that:
- Restricts answers to provided context only (no parametric knowledge).
- Limits output to 3 sentences maximum.
- Requires citing the single source_url from the highest-confidence retrieved chunk.
- Prohibits advice, comparisons, return calculations, and speculative language.

### 6.3 Grounding & hallucination control
- **Context-only answers**: System prompt + low temperature (0–0.2)
- **Citation binding**: Validator checks URL ∈ retrieved chunk metadata
- **Numeric facts**: Prefer chunks containing numbers matching query type (regex/heuristics)
- **Performance queries**: Bypass generation; return Groww scheme page link only

## 7. Query Classification & Refusal Handling
Classification runs before retrieval to avoid retrieving context that might tempt the model to compare or recommend.

### 7.1 Intent categories
- **Factual**: "What is the exit load?" -> RAG pipeline
- **Advisory**: "Should I invest?" -> Refusal
- **Comparative**: "Which fund is better?" -> Refusal
- **Performance calc**: "What returns will I get?" -> Refusal or Groww scheme page link only
- **PII / account**: "My PAN is..." -> Refusal + no storage
- **Out of scope**: Unrelated topics -> Polite boundary message

### 7.2 Classifier implementation options
Hybrid (recommended): Rules for high-confidence advisory patterns; Groq (`llama-3.1-8b-instant`) for ambiguous cases.
High-confidence refusal patterns (rule-based): should I, recommend, better fund, best fund, worth investing, buy or sell, predict, returns if I, compare.

### 7.3 Refusal response template
- Acknowledge the question politely.
- State the facts-only limitation explicitly.
- Provide one educational link (Groww mutual funds overview: https://groww.in/p/mutual-funds).
- Include standard disclaimer footer.

## 8. Response Contract
Every assistant message—factual or refusal—must satisfy:
- **≤ 3 sentences**: Sentence tokenizer + count in validator
- **Exactly 1 citation URL**: Regex URL check; must match allowed domains
- **Footer with date**: `Last updated from sources: <document_date or ingest date>`
- **Disclaimer present**: Static string in UI and/or API payload
- **No advice language**: Blocklist: recommend, should invest, better, guaranteed, predict
- **Performance-related queries**: Do not compute or state returns. Response = one sentence + Groww scheme page link.

## 9. Corpus & Source Model

### 9.1 Selected AMC and schemes
- **AMC**: HDFC Mutual Fund
- **Corpus provider**: Groww (groww.in)

### 9.2 Allowed source domains (allowlist)
- `groww.in`
- `*.groww.in`
The validator rejects citations outside this allowlist. Factual answers cite the relevant scheme page; refusals cite https://groww.in/p/mutual-funds.

### 9.3 Fact type → source mapping
All fact types resolve to the same Groww scheme page for the fund in question:
- Expense ratio, exit load, min SIP -> Groww scheme page — fund details section
- Riskometer, benchmark -> Groww scheme page — fund overview
- ELSS lock-in -> Groww scheme page — fund details / tax section
- Performance / returns -> Groww scheme page link only (no computed values)
- Statement download process -> Groww scheme page or help content (if present on page)

## 10. User Interface
Minimal single-page chat interface.

### 10.1 Layout
- Welcome message explaining scope and limitations
- Example questions (clickable)
- Chat message history (Assistant answer, Source, Last updated, Disclaimer)
- Ask a factual question input

### 10.2 UI requirements
- Persistent disclaimer banner: "Facts-only. No investment advice."
- Three pre-filled example questions (as specified in problem statement).
- Citation rendered as a clickable link opening in a new tab.
- No login, no cookies for PII, no chat export containing user identifiers.
- Mobile-friendly responsive layout.

## 11. Technology Stack
- **Backend**: Python 3.11+ / FastAPI
- **RAG orchestration**: LangChain or LlamaIndex
- **Embeddings**: Local open-source (bge-small-en via sentence-transformers)
- **Vector store**: Chroma (local) or FAISS
- **LLM**: Groq API (groq Python SDK)
- **HTML parsing**: BeautifulSoup / trafilatura; Playwright if JS-rendered
- **Frontend**: React + Vite or plain HTML/JS
- **Config**: `.env` for API keys

### 11.1 Why this stack
- Python + FastAPI: Standard for RAG prototypes.
- Local vector store: No external DB required for v1.
- Groq for generation: Low-latency inference on open models.
- Local embeddings: Keeps retrieval offline and avoids a second paid API.

### 11.2 Groq LLM integration
- Primary model: `llama-3.3-70b-versatile`
- Fast fallback/classifier: `llama-3.1-8b-instant`

## 12. Project Structure
```text
rag-chatbot/
├── docs/
│   ├── problemStatement.md
│   └── Architecture.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── index/
├── src/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   ├── api/
│   └── config/
├── frontend/
├── scripts/
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## 13. Security, Privacy & Compliance
- **Data handling**: Ephemeral processing; PAN/Aadhaar/OTP never accepted or stored.
- **Input sanitization**: Reject payloads containing PII patterns, rate-limit /chat.
- **Content compliance**: No personalized investment advice, no rankings, performance questions linked only.

## 14. Deployment Model
### 14.1 Development
```bash
# Terminal 1 — API
uvicorn src.api.main:app --reload --port 8000
# Terminal 2 — Frontend (static)
python -m http.server 5173 -d frontend
```

### 14.2 Production (optional)
- API: Docker container on Railway / Render / Fly.io
- Frontend: Static hosting (Vercel, Netlify, S3)
- Vector index: Baked into container image or mounted volume

## 15. Observability & Quality
Track retrieval hit rate, refusal rate, validator rejection rate, response latency.
Maintain an evaluation set of ~20 factual Q&A pairs.

## 16. Known Limitations
- Corpus covers only 5 HDFC schemes
- Groww page content updates; answers may stale
- Groww HTML/JS rendering may block simple fetch
- Classifier may miss subtle advisory phrasing
- No real-time fetch from Groww at query time

## 17. Future Extensions (Out of Scope)
- Multi-AMC corpus expansion
- Live Groww page fetch at query time
- Cross-encoder reranking for improved retrieval
- Admin dashboard for ingest status and source freshness
- Multilingual support (Hindi)
- Voice interface
