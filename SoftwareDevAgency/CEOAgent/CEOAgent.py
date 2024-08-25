from agency_swarm.agents import Agent


class CEOAgent(Agent):
    def __init__(self):
        super().__init__(
            name="CEOAgent",
            description="The CEO agent oversees the entire software development process and coordinates between agents within the SoftwareDevAgency. It ensures seamless communication and collaboration between the Requirements Analyst, UI/UX Designer, and Developer agents.",
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
