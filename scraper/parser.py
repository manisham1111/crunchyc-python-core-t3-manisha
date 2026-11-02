
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def parse_books(html, base_url):
    """Extract book details from a listing page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title_tag = book.select_one("h3 a")
        price_tag = book.select_one(".price_color")
        availability_tag = book.select_one(".availability")
        rating_tag = book.select_one(".star-rating")

        title = title_tag.get("title", "").strip() if title_tag else "Unknown"
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        availability = availability_tag.get_text(strip=True) if availability_tag else "Unknown"
        rating = "Unknown"

        if rating_tag:
            rating_classes = rating_tag.get("class", [])
            rating = next(
                (item for item in rating_classes if item != "star-rating"),
                "Unknown"
            )

        product_url = (
            urljoin(base_url, title_tag.get("href"))
            if title_tag else ""
        )

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "url": product_url
        })

    return books

def get_next_page(html, current_url):
    soup = BeautifulSoup(html, "html.parser")

    next_link = soup.select_one("li.next a")

    if next_link:
        return urljoin(current_url, next_link.get("href"))

    return None
