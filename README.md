# Web-Crawler-Using-Multithreading

This is a multi-threaded web crawler implemented in Python using the `multiprocessing`, `threading`, and `requests` libraries. It allows you to scrape information and links from web pages in parallel, utilizing the power of multiple threads.

## Features

- Multi-threaded crawling for faster scraping of web pages.
- Parses HTML content to extract links and information.
- Handles relative and absolute URLs using `urljoin`.
- Uses a thread pool to manage worker threads efficiently.
- Prints out scraped text content from web pages.
- Provides insights about the seed URL and scraped pages.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/dhruvsoni0612/Web-Crawler-Using-Multithreading.git

2. Install Dependencies:

   ```bash
   pip install requests beautifulsoup4

3. Run main.py
