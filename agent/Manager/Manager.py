from agency_swarm.agents import Agent

DESCRIPTION = (
    "You are a manager agent. You direct the actions of the researcher agent."
    "You are responsible for creating plans and strategies, coordinating activities, and compiling the final response."
)

class Manager(Agent):
    def __init__(self):
        super().__init__(
            name="Manager",
            description=DESCRIPTION,
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
