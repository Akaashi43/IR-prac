# challenges_such_as_robotstxt

import requests
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from urllib.parse import urlparse, urljoin
class WebCrawler:
    def __init__(self, seed_url, max_pages=50, delay=3, chrome_driver_path="path_to_chromedriver"):
        self.seed_url = seed_url
        self.max_pages = max_pages
        self.visited_urls = set()
        self.url_index = {}
        self.to_visit = [seed_url]
        self.delay_time = delay
        self.chrome_driver_path = chrome_driver_path
        self.robot_parser = RobotFileParser()
    def is_allowed_to_crawl(self, url):
        domain = urlparse(url).netloc
        robots_url = f"https://{domain}/robots.txt"
        
        try:
            self.robot_parser.set_url(robots_url)
            self.robot_parser.read()
            return self.robot_parser.can_fetch("*", url)  
        except:
            print(f"Could not fetch robots.txt for {domain}, assuming no restrictions.")
            return True 

    def fetch_page(self, url):
        if not self.is_allowed_to_crawl(url):
            print(f"Blocked by robots.txt: {url}")
            return None
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch page: {url} (Status Code: {response.status_code})")
                return None
        except requests.RequestException as e:
            print(f"Error fetching page {url}: {e}")
            return self.fetch_dynamic_content(url)
    def fetch_dynamic_content(self, url):
        options = Options()
        options.headless = True  
        service = Service(self.chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        time.sleep(self.delay_time)  
        page_content = driver.page_source
        driver.quit()

        return page_content

    def parse_page(self, html, url):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        text = ' '.join([p.get_text() for p in soup.find_all('p')]).strip()
        links = set()
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href.startswith('http'):
                links.add(href)
            else:
                links.add(urljoin(url, href))
        return title, text, links
    def index_page(self, url, title, text):
        self.url_index[url] = {'title': title, 'text': text}
        print(f"Indexed: {url}")
    def crawl(self):
        while self.to_visit and len(self.visited_urls) < self.max_pages:
            url = self.to_visit.pop(0)

            if url in self.visited_urls:
                continue
            print(f"Crawling: {url}")
            self.visited_urls.add(url)
            page_content = self.fetch_page(url)
            if page_content:
                title, text, links = self.parse_page(page_content, url)
                self.index_page(url, title, text)
                for link in links:
                    if link not in self.visited_urls and link not in self.to_visit:
                        self.to_visit.append(link)
            time.sleep(self.delay_time)
        print(f"Crawling finished. Visited {len(self.visited_urls)} pages.")
    def display_index(self):
        print("\nIndexed Pages:")
        for url, data in self.url_index.items():
            print(f"URL: {url}")
            print(f"Title: {data['title']}")
            print(f"Text snippet: {data['text'][:100]}...\n")
seed_url = 'https://example.com'  
chrome_driver_path = 'path_to_chromedriver'  
crawler = WebCrawler(seed_url, max_pages=10, delay=3, chrome_driver_path=chrome_driver_path)
crawler.crawl()
crawler.display_index()
