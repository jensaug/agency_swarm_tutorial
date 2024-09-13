from agency_swarm.agents import Agent

description = (
    "You are an expert in the energy field. You are responsible for finding energy data."
)

class EnergyExpert(Agent):
    def __init__(self):
        super().__init__(
            name="EnergyExpert",
            description=description,
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000
        )
