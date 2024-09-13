import json
import os
import requests
from agency_swarm.tools import BaseTool
from pydantic import Field
#from utils import load_config

#load_config(file_path="./config.yaml")

class SearchEngine(BaseTool):
    """
    SearchEngine: A search engine tool. You can use this tool to search for a specific query on a search engine.
    The output of the search engine is a dictionary where the key is the source of the information and the value is the content.
    """
    search_engine_query: str = Field(
        ..., description= "Search engine query to be executed by the tool"
    )



    def format_results(self, organic_results):

        result_strings = []
        for result in organic_results:
            title = result.get('title', 'No Title')
            link = result.get('link', '#')
            snippet = result.get('snippet', 'No snippet available.')
            result_strings.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n---")
        
        return '\n'.join(result_strings)

    def run(self):

        search_url = "https://google.serper.dev/search"
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': os.environ['SERPER_DEV_API_KEY']  # Ensure this environment variable is set with your API key
        }
        payload = json.dumps({"q": self.search_engine_query})
        
        # Attempt to make the HTTP POST request
        try:
            response = requests.post(search_url, headers=headers, data=payload)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4XX, 5XX)
            results = response.json()
            
            # Check if 'organic' results are in the response
            if 'organic' in results:
                return self.format_results(results['organic'])
            else:
                return "No organic results found."

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.RequestException as req_err:
            return f"Request exception occurred: {req_err}"
        except KeyError as key_err:
            return f"Key error in handling response: {key_err}"