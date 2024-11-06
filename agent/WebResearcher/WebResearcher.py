from agency_swarm.agents import Agent

description = (
    "You are a researcher agent. You are responsible for conducting general research tasks."
)

class WebResearcher(Agent):
    def __init__(self):
        super().__init__(
            name="WebResearcher",
            description=description,
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-4o-mini-2024-07-18"
        )
