import os
import glob
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.config.schemes import SCHEMES

PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")
INDEX_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "index")

def get_metadata(filename):
    basename = os.path.splitext(os.path.basename(filename))[0]
    if basename in SCHEMES:
        meta = SCHEMES[basename].copy()
        meta["document_type"] = "groww_scheme_page"
        meta["source_domain"] = "groww.in"
        # We don't have exact last_updated from page, so we use a placeholder or omit
        meta["document_date"] = "2026-08-30" 
        return meta
    return {}

def index_documents():
    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    
    text_files = glob.glob(os.path.join(PROCESSED_DATA_DIR, "*.txt"))
    all_chunks = []
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", " "]
    )
    
    for file_path in text_files:
        print(f"Processing {os.path.basename(file_path)}...")
        loader = TextLoader(file_path, encoding="utf-8")
        docs = loader.load()
        
        metadata = get_metadata(file_path)
        for doc in docs:
            doc.metadata.update(metadata)
            
        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)
        
    print(f"Total chunks generated: {len(all_chunks)}")
    print("Upserting into ChromaDB...")
    
    vectorstore = Chroma.from_documents(
        documents=all_chunks,
        embedding=embeddings,
        persist_directory=INDEX_DIR,
        collection_name="mutual_funds"
    )
    
    # chromadb 0.4.x auto-persists, but we can call it if it exists
    if hasattr(vectorstore, 'persist'):
        vectorstore.persist()
        
    print("Indexing complete.")

if __name__ == "__main__":
    index_documents()
