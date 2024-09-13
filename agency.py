import os
from agency_swarm import Agency, set_openai_key
from agent.EnergyExpert import EnergyExpert
from agent.Manager import Manager
from agent.WebResearcher import WebResearcher

# loads API keys from config.yaml
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
set_openai_key(OPENAI_API_KEY)

MISSION_STATEMENT = (
    "You are a team of agents working together on research tasks.\n"
    "The team consists of a manager, a researcher and an energy expert.\n"
    "The manager asks the energy expert for data relating to energy consumption"
    "The manager creates a plan for the researcher to follow.\n"
    "The energy expert finds data on energy consumption."
    "The researcher conducts research using the tools available.\n"
    "The manager compiles the research and findings into a final response.\n"
    "You must work together to complete the task at hand.\n"
)
# def get_current_utc_datetime():
#     now_utc = datetime.now(timezone.utc)
#     current_time_utc = now_utc.strftime("%Y-%m-%d %H:%M:%S %Z")
#     return current_time_utc

manager = Manager()
energyExpert = EnergyExpert()
webResearcher = WebResearcher()

agency = Agency([
       manager,
       [manager, energyExpert],
       [manager, webResearcher]
     ], 
     shared_instructions= MISSION_STATEMENT,
     temperature=0,
)

if __name__ == "__main__":
    agency.run_demo()