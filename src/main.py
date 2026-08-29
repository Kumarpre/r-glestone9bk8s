from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime
import sys
import os

# Add the root directory to path to ensure modules can be imported if run directly
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.generation.classifier import QueryClassifier
from src.generation.generator import ResponseGenerator
from src.generation.validator import ResponseValidator
from src.generation.refusals import RefusalHandler
from src.retrieval.retriever import MutualFundRetriever

app = FastAPI(title="Mutual Fund FAQ Assistant API")

# Allow CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
classifier = QueryClassifier()
retriever = MutualFundRetriever(k=4, max_distance=1.2)
generator = ResponseGenerator()
validator = ResponseValidator(max_sentences=3)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
    category: str

@app.get("/health")
def health_check():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    query = request.query
    
    # 1. Classify
    classification = classifier.classify(query)
    category = classification.get("category", "FACTUAL")
    
    # 2. Check for Refusal
    if category in ["ADVICE", "COMPARISON"]:
        refusal = RefusalHandler.get_refusal(category)
        return ChatResponse(answer=refusal, category=category)
        
    # 3. Retrieve
    chunks = retriever.retrieve(query)
    
    # 4. Generate
    gen_result = generator.generate(query, chunks)
    raw_answer = gen_result.get("answer")
    source_url = gen_result.get("source_url")
    
    # Extract document date from the best chunk if available
    doc_date = None
    if chunks and chunks[0].get("metadata"):
        doc_date = chunks[0]["metadata"].get("document_date")
    
    # 5. Validate and format
    final_answer = validator.validate_and_format(raw_answer, source_url, doc_date)
    
    return ChatResponse(answer=final_answer, category=category)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8080, reload=True)
