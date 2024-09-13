import os
import requests
from agency_swarm.tools import BaseTool
from pydantic import Field


class ElectricityMapPowerBreakdown(BaseTool):
    """
    ElectricityMapPowerBreakdown: A tool for fetcing power breakdowns. You can use this tool to get data for power consumption breakdowns for different zone abbreviations.
    You must provide the zone abbreviation in uppercase
    The source for this information is "https://api.electricitymap.org/v3/power-breakdown/latest?zone=${zone}", where ${zone} is the provide zone abbreviation in uppercase
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