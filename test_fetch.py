
from scraper.fetcher import fetch_page

url = "https://books.toscrape.com/"
html = fetch_page(url)

print("Page fetched successfully!")
print("HTML length:", len(html))
print(html[:300])
