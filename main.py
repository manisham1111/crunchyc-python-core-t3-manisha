
import logging

from scraper.fetcher import fetch_page
from scraper.parser import parse_books, get_next_page
from scraper.exporter import export_csv, export_json

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    url = "https://books.toscrape.com/"
    all_books = []
    max_books = 200

    while url and len(all_books) < max_books:
        logging.info("Fetching page: %s", url)

        html = fetch_page(url)
        books = parse_books(html, url)

        all_books.extend(books)
        print(f"Collected: {len(all_books)} books")

        url = get_next_page(html, url)

    all_books = all_books[:max_books]

    export_csv(all_books)
    export_json(all_books)

    logging.info("Scraping completed: %s books", len(all_books))
    print(f"\nTotal books collected: {len(all_books)}")


if __name__ == "__main__":
    main()
