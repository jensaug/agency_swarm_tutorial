import os
from agency_swarm import Agency, set_openai_key
from agent.AccidentAnalyst import AccidentAnalyst
from agent.EnergyExpert import EnergyExpert
from agent.JensAssistant import JensAssistant
from agent.Manager import Manager
from agent.WebResearcher import WebResearcher

# loads API keys from config.yaml
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
set_openai_key(OPENAI_API_KEY)

MISSION_STATEMENT = (
    "You are a team of agents working together on research tasks.\n"
    "The manager compiles the research and findings into a final response.\n"
    "You must work together to complete the task at hand.\n"
)

manager = Manager()
webResearcher = WebResearcher()
energyExpert = EnergyExpert()
jensAssistant = JensAssistant()
accidentAnalyst = AccidentAnalyst()

agency = Agency([
        manager,                    # No RAG
       [manager, webResearcher],    # RAG using Internet search and scrape 
       [manager, energyExpert],     # RAG using HTTP API
       [manager, jensAssistant],    # RAG using local documents
       [manager, accidentAnalyst]   # RAG using SQL data
     ],
     shared_instructions= MISSION_STATEMENT,
     temperature=0,
)

if __name__ == "__main__":
    #agency.run_demo()
    agency.demo_gradio(height=900)