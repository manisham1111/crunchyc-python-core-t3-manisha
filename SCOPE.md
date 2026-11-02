\# SCOPE.md – Ethical Web Scraping



\## Project

Books to Scrape – Public Demo Website Scraper



\## Target Website

https://books.toscrape.com/



\## Purpose

This project collects publicly available book information for educational purposes, including book titles, prices, availability, ratings, and product links.



\## Permission and Scope

Books to Scrape is a demo website created specifically for web scraping practice. It does not contain real commercial transactions.



\## robots.txt

Target: https://books.toscrape.com/robots.txt



Before scraping, robots.txt and website terms will be checked. Only permitted public pages will be accessed.



\## Data Collected

\- Book title

\- Price

\- Availability

\- Rating

\- Product URL



No personal or sensitive information will be collected.



\## Rate Limiting

\- Maximum one request every 2 seconds.

\- A real User-Agent header will be used.

\- HTTP 429 responses will be respected.

\- Exponential backoff will be used for retries.

\- No concurrent aggressive requests.



\## Pages Accessed

Only public book listing pages and pagination links will be accessed.



\## Not Allowed

\- Login-protected content

\- Personal information

\- CAPTCHA bypass

\- Ignoring robots.txt

\- Excessive requests

\- Unauthorized data collection



\## Commercial Considerations

For commercial use, I would verify licensing and written permission, review applicable laws and terms, use an official API where available, and implement stricter rate limits and data retention controls.



\## Conclusion

This project is limited to educational scraping of a public demo website with responsible request behavior.



