import os
from agency_swarm import Agency, set_openai_key

from agent.AccidentAnalyst import AccidentAnalyst
from agent.EnergyExpert import EnergyExpert
#from agent.jens import JensAssistant
from agent.Manager import Manager
from agent.WebResearcher import WebResearcher

# loads API keys from config.yaml
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
set_openai_key(OPENAI_API_KEY)

MISSION_STATEMENT = (
    "Agents in this agency work together on tasks related to general research, energy consumption and statistics about accidents."
    "An agent should only handle a task it has specific tools to work with, except for the Manager agent who may handle general tasks."
    "The Manager agent compiles the findings into a final response."
    "This agency is specific about sources of information"
)
    
manager = Manager()                 # No RAG
webResearcher = WebResearcher()     # RAG using Internet search and scrape
energyExpert = EnergyExpert()       # RAG using HTTP API
accidentAnalyst = AccidentAnalyst() # RAG using dynamic SQL data
#jensAssistant = JensAssistant()     # RAG using local documents

agency = Agency([
        manager,
       [manager, webResearcher],
       [manager, energyExpert],
       [manager, accidentAnalyst]
#       [manager, jensAssistant],    
     ],
     shared_instructions= MISSION_STATEMENT,
     temperature=0,
)

if __name__ == "__main__":
    #agency.run_demo()
    agency.demo_gradio(height=900)