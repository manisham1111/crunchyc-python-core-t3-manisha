
import requests
import time

HEADERS = {
    "User-Agent": "StudentEducationalScraper/1.0"
}


def fetch_page(url):
    """Fetch a public webpage responsibly with retries."""
    for attempt in range(3):
        try:
            time.sleep(2)

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=15
            )

            if response.status_code == 429:
                wait_time = 2 ** (attempt + 1)
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()
            return response.content.decode("utf-8", errors="replace")

        except requests.RequestException as error:
            print(f"Request failed: {error}")
            time.sleep(2 ** (attempt + 1))

    raise RuntimeError(f"Unable to fetch: {url}")
