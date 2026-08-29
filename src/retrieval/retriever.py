import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.config.schemes import SCHEMES

INDEX_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "index")

class MutualFundRetriever:
    def __init__(self, k=4, max_distance=1.2):
        self.embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
        self.vectorstore = Chroma(
            persist_directory=INDEX_DIR, 
            embedding_function=self.embeddings,
            collection_name="mutual_funds"
        )
        self.k = k
        # max_distance threshold (Chroma L2 distance default)
        self.max_distance = max_distance

    def detect_scheme(self, query: str) -> str:
        query_lower = query.lower()
        if "mid" in query_lower:
            return "hdfc-mid-cap-fund-direct-growth"
        elif "small" in query_lower:
            return "hdfc-small-cap-fund-direct-growth"
        elif "gold" in query_lower:
            return "hdfc-gold-etf-fund-of-fund-direct-plan-growth"
        elif "large" in query_lower:
            return "hdfc-large-cap-fund-direct-growth"
        elif "elss" in query_lower or "tax" in query_lower:
            return "hdfc-elss-tax-saver-fund-direct-plan-growth"
        return None

    def retrieve(self, query: str, scheme_id: str = None) -> list:
        if not scheme_id:
            scheme_id = self.detect_scheme(query)
            
        search_kwargs = {"k": self.k}
        if scheme_id:
            search_kwargs["filter"] = {"scheme_id": scheme_id}
            
        results = self.vectorstore.similarity_search_with_score(query, **search_kwargs)
        
        valid_chunks = []
        for doc, score in results:
            # lower score means closer distance in L2
            if score <= self.max_distance:
                valid_chunks.append({
                    "content": doc.page_content,
                    "metadata": doc.metadata,
                    "score": score
                })
        
        return valid_chunks

if __name__ == "__main__":
    retriever = MutualFundRetriever()
    
    test_queries = [
        "What is the expense ratio for HDFC Small Cap?",
        "Tell me the exit load for the gold fund",
        "Does this fund have a riskometer?", # Generic question, no scheme detected
        "How to build a rocket?" # Out of scope
    ]
    
    for q in test_queries:
        print("-" * 60)
        print(f"Query: '{q}'")
        results = retriever.retrieve(q)
        print(f"Retrieved {len(results)} valid chunks.")
        for i, res in enumerate(results):
            print(f"  [{i+1}] Score: {res['score']:.4f} | Scheme: {res['metadata'].get('scheme_name')} | Length: {len(res['content'])}")
