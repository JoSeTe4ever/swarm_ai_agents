from agency_swarm.agents import Agent
from FrontendDeveloperAgent.models.InterpretedImageResponse import InterpretedImageResponse

class FrontendDeveloperAgent(Agent):
    def __init__(self):
        super().__init__(
            name="FrontendDeveloperAgent",
            description="This agent takes a picture reads it, undestands it, and generate 3 files (html js and css) that represent this image",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            response_format=InterpretedImageResponse
        )
        
    def response_validator(self, message):
        return message
