import json
import requests
from pydantic import Field
from agency_swarm.tools import BaseTool

class LocalDocuments(BaseTool):

    """
    LocalDocuments: A tool for looking gathering information using a local model.
    You must provide the content for the local model
    The source for this information is "https://api.electricitymap.org/v3/power-breakdown/latest?zone=${zone}", where ${zone} is the provide zone abbreviation in uppercase
    The output of this tool is a dictionary where the key is the source of the information and the value is the content.
    """
    zone: str = Field(
        ..., content= "The content for the local model"
    )    

    def run(self):

        search_url = "http://localhost:4891/v1/chat/completions"
        payload = json.dumps({"messages": "Yo"})
        #payload = json.dumps({"messages": [{"role":"user", "content": self.content}]})
        return requests.post(search_url, data=payload).json()