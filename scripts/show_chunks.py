import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import json

INDEX_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "index")

def show_chunks():
    print(f"Connecting to ChromaDB at {INDEX_DIR}...")
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    vectorstore = Chroma(
        persist_directory=INDEX_DIR, 
        embedding_function=embeddings,
        collection_name="mutual_funds"
    )
    
    # Get total count
    count = vectorstore._collection.count()
    print(f"\nTotal chunks stored in ChromaDB: {count}")
    
    print("\nFetching 1 sample chunk from the database:")
    print("-" * 50)
    
    # We can do a dummy similarity search to get a chunk
    results = vectorstore.similarity_search("expense ratio", k=1)
    
    if results:
        doc = results[0]
        print(f"Content:\n{doc.page_content}")
        print("-" * 50)
        print(f"Metadata:\n{json.dumps(doc.metadata, indent=2)}")
    else:
        print("No chunks found!")

if __name__ == "__main__":
    show_chunks()
