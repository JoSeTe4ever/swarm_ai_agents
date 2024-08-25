from agency_swarm.agents import Agent


class RequirementsAnalystAgent(Agent):
    def __init__(self):
        super().__init__(
            name="RequirementsAnalystAgent",
            description="The Requirements Analyst agent is responsible for gathering and analyzing software requirements within the SoftwareDevAgency. It communicates with the CEO and UI/UX Designer agents to ensure accurate and comprehensive requirement analysis.",
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
