from agency_swarm.tools import BaseTool
from pydantic import Field
import openai
import os

# Define a global variable for the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

class DesignGenerationTool(BaseTool):
    """
    This tool interfaces with DALL-E 3 to generate UI/UX designs based on the requirements provided by the Requirements Analyst Agent.
    It allows the agent to input design prompts and receive generated images as output.
    """

    design_prompt: str = Field(
        ..., description="The design prompt describing the UI/UX design requirements."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        if not openai_api_key:
            return "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."

        # Set the OpenAI API key
        openai.api_key = openai_api_key

        try:
            # Generate the design using DALL-E 3
            response = openai.images.generate(
                prompt=self.design_prompt,
                n=1,
                size="1024x1024"
            )

            # Extract the URL of the generated image
            image_url = response.data[0].url
            self._shared_state.set("image_url", image_url)

            return f"Design generated successfully. Image URL: {image_url}"

        except Exception as e:
            return f"An error occurred while generating the design: {str(e)}"