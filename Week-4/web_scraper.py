import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_page(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                print("✅ Page fetched successfully.")
                return response.text
            else:
                print("❌ Failed to fetch the page.")
                return None
        except Exception as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_headlines(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        # BBC example: headlines inside <h3> with class
        headlines = soup.find_all(['h1', 'h2', 'h3'])
        extracted = []

        for h in headlines:
            text = h.get_text(strip=True)
            if text and len(text) > 15:  # filter short or empty text
                extracted.append(text)

        return extracted

    def run(self):
        html = self.fetch_page()
        if html:
            headlines = self.parse_headlines(html)
            if headlines:
                print("\n📰 Headlines Found:")
                for i, headline in enumerate(headlines[:10], 1):  # limit to 10
                    print(f"{i}. {headline}")
            else:
                print("⚠️ No headlines found.")
        else:
            print("⚠️ Could not retrieve HTML content.")

# --- Run the scraper ---
if __name__ == "__main__":
    url = "https://www.bbc.com/news"  # Try another news site if needed
    scraper = WebScraper(url)
    scraper.run()
