import os
import glob
from bs4 import BeautifulSoup
import re

RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")

def clean_text(text):
    # Normalize unicode and whitespace
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def parse_html_to_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove noisy tags
    for element in soup(["script", "style", "nav", "footer", "noscript", "svg", "header", "button", "iframe"]):
        element.decompose()
        
    # Extract text with a newline separator keeps block elements somewhat separated
    text = soup.get_text(separator='\n', strip=True)
    return clean_text(text)

def process_all():
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    raw_files = glob.glob(os.path.join(RAW_DATA_DIR, "*.html"))
    
    for file_path in raw_files:
        basename = os.path.basename(file_path)
        name = os.path.splitext(basename)[0]
        
        print(f"Parsing {basename}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        text = parse_html_to_text(html)
        
        out_path = os.path.join(PROCESSED_DATA_DIR, f"{name}.txt")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved processed text to {out_path}")

if __name__ == "__main__":
    process_all()
