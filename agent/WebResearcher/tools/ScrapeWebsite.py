import json
import requests
from agency_swarm.tools import BaseTool
from pydantic import Field
from bs4 import BeautifulSoup


class ScrapeWebsite(BaseTool):
    """
    This is a website scraping tool. You can use this tool to scrape the content of a website.
    You must provide the URL of the website you want to scrape.
    """
    website_url: str = Field(
        ..., description= "The URL of the website to scrape the content from."
    )

    def run(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        
        try:
            # Making a GET request to the website
            response = requests.get(self.website_url, headers=headers, timeout=15)
            response.raise_for_status()  # This will raise an exception for HTTP errors

            # Parsing the page content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text(separator='\n')
            # Cleaning up the text: removing excess whitespace
            clean_text = '\n'.join([line.strip() for line in text.splitlines() if line.strip()])

            print(f"Successfully scraped content from {self.website_url}")

            return {self.website_url: clean_text[:1048000]}

        except requests.exceptions.RequestException as e:
            print(f"Error retrieving content from {self.website_url}: {e}")
            return {self.website_url: f"Failed to retrieve content due to an error: {e}"}