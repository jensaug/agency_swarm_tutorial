import json
import os
import requests
from agency_swarm.tools import BaseTool
from pydantic import Field

class SearchEngine(BaseTool):
    """
    This is a search engine tool. You can use this tool to execute queries on a web search engine.
    The output of the web search engine is a dictionary where the key is the source of the information and the value is the content.
    """
    search_engine_query: str = Field(
        ..., description= "Search engine query text to be executed by the tool"
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
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.RequestException as req_err:
            return f"Request exception occurred: {req_err}"
        except KeyError as key_err:
            return f"Key error in handling response: {key_err}"