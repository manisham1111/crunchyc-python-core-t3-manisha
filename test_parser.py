
from scraper.fetcher import fetch_page
from scraper.parser import parse_books

url = "https://books.toscrape.com/"
html = fetch_page(url)

books = parse_books(html, url)

print("Books found:", len(books))
print(books[0])
