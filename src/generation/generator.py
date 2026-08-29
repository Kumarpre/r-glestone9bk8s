import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.retry import exponential_backoff

load_dotenv()

class ResponseGenerator:
    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.model = os.environ.get("MODEL_GENERATOR", "gemini-2.5-flash")

    @exponential_backoff(max_retries=3, base_delay=2)
    def generate(self, query: str, context_chunks: list) -> dict:
        if not context_chunks:
            return {
                "answer": "I do not have enough factual information in my knowledge base to answer that question.",
                "source_url": "https://groww.in/p/mutual-funds"
            }
            
        # Format the context
        context_text = "\n\n---\n\n".join([c["page_content"] for c in context_chunks])
        source_url = context_chunks[0]["metadata"].get("source_url", "https://groww.in/p/mutual-funds")

        prompt = f"""
You are a highly constrained, facts-only Mutual Fund Assistant.
Your task is to answer the user's query strictly using the provided context chunks.

RULES:
1. FACTS ONLY: Do not provide any investment advice, predictions, or opinions.
2. STRICT LIMIT: Your response MUST NOT exceed 3 sentences.
3. NO OUTSIDE KNOWLEDGE: If the context does not contain the answer, say "I cannot find this information in my current documents."
4. NO MARKDOWN: Do not use bold, italics, or lists. Return plain text only.

Context:
{context_text}

User Query:
{query}
"""
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return {
                "answer": response.text.strip(),
                "source_url": source_url
            }
        except Exception as e:
            print(f"Generator error: {e}")
            return {
                "answer": "I am currently unable to generate a response due to an internal error.",
                "source_url": source_url
            }
