\# Ethical Web Scraper – Python



\## Project Overview

A Python-based ethical web scraper built using Requests and BeautifulSoup. It collects book information from Books to Scrape demo website and exports the extracted data into CSV and JSON formats.



\## Features

\- Fetch webpages using Requests

\- Parse HTML using BeautifulSoup

\- Pagination support

\- Retry mechanism with exponential backoff

\- HTTP 429 rate-limit handling

\- Missing data handling

\- CSV and JSON export

\- Scraping logs



\## Tech Stack

\- Python 3.12

\- Requests

\- BeautifulSoup4



\## Installation



```bash

pip install -r requirements.txt

```



\## Run Project



```bash

python main.py

```



\## Output

\- `output/books.csv`

\- `output/books.json`

\- `logs/scraper.log`



\## Ethical Scraping

\- Uses a public demo website

\- Includes request delays

\- Uses a custom User-Agent

\- Handles rate limits responsibly

\- Avoids login-protected or private data



\## Author

Manisha M



\## Website

https://books.toscrape.com/



