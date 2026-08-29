import re
from datetime import datetime

class ResponseValidator:
    def __init__(self, max_sentences=3):
        self.max_sentences = max_sentences

    def validate_and_format(self, raw_answer: str, source_url: str, document_date: str = None) -> str:
        """
        Validates the raw answer and appends the mandatory citation and footer.
        """
        # 1. Enforce max 3 sentences
        # Simple regex to split by ., ?, ! followed by space or end of string
        sentences = re.split(r'(?<=[.!?]) +', raw_answer.strip())
        
        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]
        
        # Truncate if it exceeds 3 sentences
        if len(sentences) > self.max_sentences:
            sentences = sentences[:self.max_sentences]
            
        validated_answer = " ".join(sentences)
        
        # 2. Enforce citation and footer compliance
        if not source_url or not source_url.startswith("https://groww.in/"):
            source_url = "https://groww.in/p/mutual-funds"
            
        if not document_date:
            document_date = datetime.now().strftime("%Y-%m-%d")
            
        formatted_response = f"{validated_answer}\n\nSource: {source_url}\nLast updated from sources: {document_date}"
        
        return formatted_response

if __name__ == "__main__":
    validator = ResponseValidator()
    # Test case with 5 sentences
    raw = "The expense ratio is 0.5%. The exit load is 1% if redeemed within 1 year. The fund is highly rated. It has high returns. You should buy it."
    print("--- Test Validation ---")
    print(validator.validate_and_format(raw, "https://groww.in/mutual-funds/hdfc-mid-cap-fund-direct-growth", "2026-08-30"))
