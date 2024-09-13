from agency_swarm.tools import BaseTool
from pydantic import Field
import base64
import os
import requests

from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") # or access_token = os.getenv("MY_ACCESS_TOKEN")
print('api_key -> ' , api_key)



class ImageToCode(BaseTool):
    """
    This tool allows to interpret, read and watch an image (obtained from a url in the param image_url) and 
    return a string that represents HTML js and CSS. Use shared_image_url from shared_state when present.
    """
    
    def run(self):
        """
        Encodes the image represented in shared_image_url the OpenAI API to get code
        that represents the image (HTML, JavaScript, and CSS).
        """

        if not api_key:
            print("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
            return "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
        
        # Prepare the headers and payload for the API request

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        shared_image_url = self._shared_state.get("image_url")
        print('JOPI -> ' , shared_image_url)
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
                                "url": shared_image_url
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



if __name__ == "__main__":
    # create a ImageToCode instance
    tool = ImageToCode()
    image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-0sfjRM1BH1TpAhFDzutPncf2/user-dh8jqRtli6W5hOQx1h3v3Ppx/img-MeAMkTLt5eUq83OkPifP2cvn.png?st=2024-09-13T08%3A07%3A53Z&se=2024-09-13T10%3A07%3A53Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-12T23%3A14%3A21Z&ske=2024-09-13T23%3A14%3A21Z&sks=b&skv=2024-08-04&sig=NYaTrk8gWY3WOP6wE/YMJecAOCbzDEpR/O3vSqHqDjI%3D"
    tool._shared_state.set("image_url", image_url)
    tool.run()