import urllib.request
import os
import time

URLS = {
    "hdfc-mid-cap": "https://groww.in/mutual-funds/hdfc-mid-cap-fund-direct-growth",
    "hdfc-small-cap": "https://groww.in/mutual-funds/hdfc-small-cap-fund-direct-growth",
    "hdfc-gold-etf": "https://groww.in/mutual-funds/hdfc-gold-etf-fund-of-fund-direct-plan-growth",
    "hdfc-large-cap": "https://groww.in/mutual-funds/hdfc-large-cap-fund-direct-growth",
    "hdfc-elss-tax-saver": "https://groww.in/mutual-funds/hdfc-elss-tax-saver-fund-direct-plan-growth"
}

RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")

def fetch_and_save():
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    for name, url in URLS.items():
        print(f"Fetching {name} from {url}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                
            file_path = os.path.join(RAW_DATA_DIR, f"{name}.html")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Saved {name} to {file_path}")
            
            # Sleep to prevent getting blocked
            time.sleep(2)
        except Exception as e:
            print(f"Error fetching {name}: {e}")

if __name__ == "__main__":
    fetch_and_save()
