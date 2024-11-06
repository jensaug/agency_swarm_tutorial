import os
import requests
from agency_swarm.tools import BaseTool
from pydantic import Field


class ElectricityMapPowerBreakdown(BaseTool):
    """
    This tool can find power breakdowns for energy consumptions in different zones.
    You must provide the zone abbreviation in uppercase.
    The source for this information is "https://api.electricitymap.org/v3/power-breakdown/latest?zone=${zone}"
    The output of this tool is a dictionary where the key is the source of the information and the value is the content.
    """
    zone: str = Field(
        ..., description= "The zone abbreviation in uppercase"
    )    
    
    def run(self):
        params = {'zone': self.zone}
        search_url = "https://api.electricitymap.org/v3/power-breakdown/latest"
        headers = {
            'Content-Type': 'application/json',
            'auth-token': os.getenv("ELECTRICITY_MAP_API_KEY")
        }
        response = requests.get(search_url, params, headers=headers, timeout=10)
        return response.json()