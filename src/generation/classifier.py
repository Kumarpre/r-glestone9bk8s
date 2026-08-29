import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.retry import exponential_backoff

load_dotenv()

class QueryClassifier:
    def __init__(self):
        # We fallback to OPENAI_API_KEY just in case the user left it there
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.model = os.environ.get("MODEL_CLASSIFIER", "gemini-2.5-flash")

    @exponential_backoff(max_retries=3, base_delay=2)
    def classify(self, query: str) -> dict:
        prompt = f"""
You are a strict query classification system for a Mutual Fund assistant.
You must classify the user's query into exactly one of the following categories:
- FACTUAL: The user is asking a factual question about a specific fund's details (e.g., Expense ratio, exit load, lock-in period, AUM, NAV, SIP amount).
- ADVICE: The user is asking for investment advice, predictions, or opinions (e.g., "Is this a good fund?", "Should I invest?", "Will it go up?").
- COMPARISON: The user is asking to compare multiple funds or asking for the "best" fund.
- OUT_OF_SCOPE: The user is asking about something completely unrelated to the specific HDFC mutual funds provided.

Analyze the following query:
"{query}"

Return ONLY a valid JSON object with two keys:
"category": The category string (FACTUAL, ADVICE, COMPARISON, or OUT_OF_SCOPE)
"reasoning": A brief one sentence explanation for the classification.
"""
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                )
            )
            return json.loads(response.text)
        except Exception as e:
            print(f"Classifier error: {e}")
            return {"category": "FACTUAL", "reasoning": "Fallback due to API/Parse error"}

if __name__ == "__main__":
    classifier = QueryClassifier()
    print(classifier.classify("What is the expense ratio of HDFC Small Cap?"))
    print(classifier.classify("Should I invest in HDFC Mid Cap or is Small Cap better?"))
