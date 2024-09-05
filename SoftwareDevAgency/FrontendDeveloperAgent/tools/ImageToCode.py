from agency_swarm.tools import BaseTool
from pydantic import Field
import base64
import os
import requests

api_key = os.getenv("OPENAI_API_KEY") # or access_token = os.getenv("MY_ACCESS_TOKEN")


class ImageToCode(BaseTool):
    """
    A brief description of what the custom tool does.
    The docstring should clearly explain the tool's purpose and functionality.
    It will be used by the agent to determine when to use this tool.
    """

    # Define the fields with descriptions using Pydantic Field
    image_url: str = Field(
        ..., description="url where the image is to be found"
    )
    
    def run(self):
        """
        Encodes the local image to base64 and calls the OpenAI API to get code
        that represents the image (HTML, JavaScript, and CSS).
        """
        
        # Prepare the headers and payload for the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Transform this image into code (HTML, JavaScript, and CSS)."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": self.image_url
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        # Send the POST request to the OpenAI API
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        
        # Extract and return the generated code from the response
        print(response.json())
        
        #if (response.json()['error']):
        #    print(response.json()['error'])
        #    # check how to do this 
        
        return response.json()['choices'][0]['message']['content']
