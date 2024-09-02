from agency_swarm.agents import Agent

from UIDesginer.models.GeneratedImageResponse import GeneratedImageResponse

class UIDesginer(Agent):
    def __init__(self):
        super().__init__(
            name="UIDesginer",
            description="This agent will create a UI design using templates supplied",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            response_format=GeneratedImageResponse
        )
        
    def response_validator(self, message):
        return message
