import requests
from agency_swarm.tools import BaseTool

class StunsEnergy(BaseTool):
    """
    This is a website scraping tool. You can use this tool to scrape the content of a website.
    You must provide the URL of the website you want to scrape.
    This is the StunsEnergy tool. Use this tool to access for data about energy consumption at Tiunda school
    When using StunsEnergy tool you must select the best date and time to find the relevant energy usage.
    The source API for StunsEnergy tool is found here: https://www.dataportal.se/sv/datasets/763_1422/tiunda-skola-uppsala-energimatning-15-minuters-data/apiexplore/1415
    """
    def run(self):

        search_url = "https://stuns.entryscape.net/rowstore/dataset/5724fdc9-662b-4eb9-90da-d5490c129b75?_limit=100&_offset=0"
        headers = {
            'Content-Type': 'application/json'
        }
        return requests.get(search_url, headers=headers, timeout=10).json()