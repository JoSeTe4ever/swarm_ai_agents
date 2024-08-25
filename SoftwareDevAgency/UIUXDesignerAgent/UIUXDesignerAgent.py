from agency_swarm.agents import Agent


class UIUXDesignerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="UIUXDesignerAgent",
            description="The UI/UX Designer agent is responsible for generating innovative and user-friendly UI/UX designs using DALL-E 3 within the SoftwareDevAgency. It collaborates with the CEO, Requirements Analyst, and Developer agents to ensure designs align with project requirements and goals.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
