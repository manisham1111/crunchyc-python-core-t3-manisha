
import csv
import json
from pathlib import Path


def export_csv(books, filename="output/books.csv"):
    """Export books to CSV."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    fields = ["title", "price", "availability", "rating", "url"]

    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(books)

    print(f"CSV saved: {path}")


def export_json(books, filename="output/books.json"):
    """Export books to JSON."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)

    print(f"JSON saved: {path}")
