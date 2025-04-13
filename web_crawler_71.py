# web_crawler

import requests
from bs4 import BeautifulSoup
import re
import time
class WebCrawler:
    def __init__(self, seed_url, max_pages=50):
        self.seed_url = seed_url  
        self.max_pages = max_pages  
        self.visited_urls = set() 
        self.url_index = {}  
        self.to_visit = [seed_url]  
    def crawl(self):
        while self.to_visit and len(self.visited_urls) < self.max_pages:
            url = self.to_visit.pop(0)
            if url in self.visited_urls:
                continue
            print(f"Crawling: {url}")
            self.visited_urls.add(url)

            try:
                page_content = self.fetch_page(url)
                if page_content:
                    title, text, links = self.parse_page(page_content)
                    self.index_page(url, title, text)
                    for link in links:
                        if link not in self.visited_urls and link not in self.to_visit:
                            self.to_visit.append(link)
                time.sleep(1)  
            except Exception as e:
                print(f"Failed to fetch {url}: {e}")

        print(f"Crawling finished. Visited {len(self.visited_urls)} pages.")
    def fetch_page(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error fetching page: {url} (Status code: {response.status_code})")
                return None
        except requests.RequestException as e:
            print(f"Error fetching page {url}: {e}")
            return None
    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        text = ' '.join([p.get_text() for p in soup.find_all('p')]).strip()
        links = set()
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href.startswith('http'):
                links.add(href)
        return title, text, links
    def index_page(self, url, title, text):
        self.url_index[url] = {'title': title, 'text': text}
        print(f"Indexed: {url}")

    def display_index(self):
        print("\nIndexed Pages:")
        for url, data in self.url_index.items():
            print(f"URL: {url}")
            print(f"Title: {data['title']}")
            print(f"Text snippet: {data['text'][:100]}...\n")
seed_url = 'https://example.com'  
crawler = WebCrawler(seed_url, max_pages=10)
crawler.crawl()
crawler.display_index()
