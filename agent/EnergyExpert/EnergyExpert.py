from agency_swarm.agents import Agent

description = (
    "You are an expert in the energy field. You are responsible for finding data about energy and power consumption."
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
            max_prompt_tokens=25000,
            model="gpt-4o-mini-2024-07-18"
        )
