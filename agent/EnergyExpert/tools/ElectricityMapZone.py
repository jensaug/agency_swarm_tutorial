import os
import requests
from agency_swarm.tools import BaseTool


class ElectricityMapZone(BaseTool):
    """
    This tool can retrieve zone abbreviations for different countries and territories in the world which consumes power.
    Zone abbreviations are in uppercase for different zone names. A zone name can be a country or territory.
    The source for this API is https://api.electricitymap.org/v3/zones
    """
    
    def run(self):
        search_url = "https://api.electricitymap.org/v3/zones"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(search_url, headers=headers, timeout=10)
        return response.json()