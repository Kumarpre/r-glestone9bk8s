import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.ingestion.fetcher import fetch_and_save
from src.ingestion.parser import process_all
from src.ingestion.indexer import index_documents

def run_pipeline():
    print("Starting Data Ingestion Pipeline...")
    
    print("\n--- Phase 1: Fetching Data ---")
    fetch_and_save()
    
    print("\n--- Phase 2: Parsing Data ---")
    process_all()
    
    print("\n--- Phase 3: Indexing Data ---")
    index_documents()
    
    print("\nPipeline Complete!")

if __name__ == "__main__":
    run_pipeline()
