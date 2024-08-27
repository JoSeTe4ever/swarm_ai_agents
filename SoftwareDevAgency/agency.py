from agency_swarm import Agency
from Devid import Devid
from UIUXDesignerAgent import UIUXDesignerAgent
from RequirementsAnalystAgent import RequirementsAnalystAgent
from CEOAgent import CEOAgent
from agency_swarm import set_openai_key
from UIDesginer import UIDesginer
from UIDesginer.tools.DesignGenerationTool import  DesignGenerationTool

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API de OpenAI desde la variable de entorno
openai_api_key = os.getenv('OPENAI_API_KEY')
set_openai_key(openai_api_key)

ceo = CEOAgent()
requirements_analyst = RequirementsAnalystAgent()
uiux_designer = UIUXDesignerAgent()
developer = Devid()
ui_designer = UIDesginer()

# agency = Agency([ceo, [ceo, requirements_analyst],
#                  [ceo, uiux_designer],
#                  [ceo, developer],
#                  [requirements_analyst, uiux_designer],
#                  [uiux_designer, developer]],
#                 shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
#                 max_prompt_tokens=25000,  # default tokens in conversation for all agents
#                 temperature=0.3,  # default temperature for all agents
#                 )


agency = Agency([ui_designer, []],
                 shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                 max_prompt_tokens=25000,  # default tokens in conversation for all agents
                 temperature=0.3,  # default temperature for all agents
                 )

# code for testing the tools 
# comment and uncomment 
def test_dalle_image_generator():
    # Create an instance of the tool with a sample prompt
    dalle_tool = DesignGenerationTool(design_prompt="Create a Product page on a Ecommerce application. Take any decision you need to take without extra input.", return_base64=False)
    
    # Run the tool to generate the image
    image_url = dalle_tool.run()
    
    # Print the result (either URL or base64 string depending on the return_base64 setting)
    print(f"Generated Image URL: {image_url}")

if __name__ == '__main__':
    #agency.demo_gradio() this is for init the agency
    test_dalle_image_generator()