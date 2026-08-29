import os
import sys

# Add the parent directory to the path so we can import the src modules
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.retrieval.retriever import MutualFundRetriever

def main():
    print("\n" + "="*50)
    print("Mutual Fund RAG - Interactive Retrieval Tester")
    print("="*50)
    
    print("Loading embedding model and connecting to ChromaDB...")
    try:
        retriever = MutualFundRetriever(k=4, max_distance=1.2)
        print("Successfully connected!\n")
    except Exception as e:
        print(f"Error loading retriever: {e}")
        return

    while True:
        try:
            query = input("\nEnter your query (or 'quit' to exit): ").strip()
            if query.lower() in ['quit', 'exit', 'q']:
                break
                
            if not query:
                continue
                
            print(f"\nSearching for: '{query}'...")
            
            # Show the user what was detected
            detected_scheme = retriever.detect_scheme(query)
            if detected_scheme:
                print(f"[!] Detected specific scheme in query: {detected_scheme}")
                print(f"[!] Applying strict metadata filter for this scheme.\n")
            else:
                print(f"[!] No specific scheme detected. Searching across all funds.\n")

            results = retriever.retrieve(query)
            
            if not results:
                print("No relevant chunks found within the distance threshold (1.2).")
                continue
                
            print(f"Top {len(results)} chunks retrieved:")
            for i, res in enumerate(results):
                print(f"\n--- Chunk {i+1} ---")
                print(f"Similarity Score (L2 Distance): {res['score']:.4f} (Lower is better)")
                print(f"Source Scheme: {res['metadata'].get('scheme_name')}")
                print(f"Content Extract:\n{res['content'][:400]}...") # Printing first 400 chars to save space
                print("-" * 20)
                
        except KeyboardInterrupt:
            break
        except EOFError:
            break

    print("\nExiting interactive tester.")

if __name__ == "__main__":
    main()
