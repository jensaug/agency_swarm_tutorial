from agency_swarm.agents import Agent

description = (
    "You are an analyst of accidents on sea, on lad and in air. You are responsible for finding facts and statistics about accidents"
)

class AccidentAnalyst(Agent):
    def __init__(self):
        super().__init__(
            name="AccidentAnalyst",
            description=description,
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-4o-mini-2024-07-18"
        )
