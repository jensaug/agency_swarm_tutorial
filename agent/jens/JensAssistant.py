from agency_swarm.agents import Agent

description = (
    "You are the personal assistant of Jens Augustsson. You are responsible for finding information about him"
)

class JensAssistant(Agent):
    def __init__(self):
        super().__init__(
            name="JensAssistant",
            description=description,
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-4o-mini-2024-07-18"
        )
