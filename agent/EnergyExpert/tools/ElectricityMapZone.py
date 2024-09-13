import os
import requests
from agency_swarm.tools import BaseTool


class ElectricityMapZone(BaseTool):
    """
    ElectricityMapZone: A tool for fetcing zone abbreviations in uppercase for different zone names. A zone name can be a country or territory.
    """
    
    def run(self):
        search_url = "https://api.electricitymap.org/v3/zones"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(search_url, headers=headers, timeout=10)
        return response.json()