import requests
from agency_swarm.tools import BaseTool

class StunsEnergy(BaseTool):

    def run(self):

        search_url = "https://stuns.entryscape.net/rowstore/dataset/5724fdc9-662b-4eb9-90da-d5490c129b75?_limit=100&_offset=0"
        headers = {
            'Content-Type': 'application/json'
        }
        return requests.get(search_url, headers=headers, timeout=10).json()