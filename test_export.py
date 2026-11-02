
from scraper.fetcher import fetch_page
from scraper.parser import parse_books
from scraper.exporter import export_csv, export_json

url = "https://books.toscrape.com/"
html = fetch_page(url)

books = parse_books(html, url)

export_csv(books)
export_json(books)

print("Export completed!")
