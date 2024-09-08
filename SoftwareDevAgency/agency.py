from agency_swarm import Agency
from Devid import Devid
from FrontendDeveloperAgent import FrontendDeveloperAgent
from UIUXDesignerAgent import UIUXDesignerAgent
from RequirementsAnalystAgent import RequirementsAnalystAgent
from CEOAgent import CEOAgent
from agency_swarm import set_openai_key
from UIDesginer import UIDesginer
from UIDesginer.tools.DesignGenerationTool import  DesignGenerationTool
from FrontendDeveloperAgent.tools.ImageToCode import  ImageToCode

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
fe_developer = FrontendDeveloperAgent()

# agency = Agency([ceo, [ceo, requirements_analyst],
#                  [ceo, uiux_designer],
#                  [ceo, developer],
#                  [requirements_analyst, uiux_designer],
#                  [uiux_designer, developer]],
#                 shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
#                 max_prompt_tokens=25000,  # default tokens in conversation for all agents
#                 temperature=0.3,  # default temperature for all agents
#                 )


agency = Agency([ui_designer, [fe_developer]],
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

def test_image2code():
    # Create an instance of the tool with a sample prompt
    image2code_tool = ImageToCode(image_url="https://oaidalleapiprodscus.blob.core.windows.net/private/org-0sfjRM1BH1TpAhFDzutPncf2/user-dh8jqRtli6W5hOQx1h3v3Ppx/img-dQ5ACy7HD46kf00Ss0RHgeSr.png?st=2024-09-05T13%3A56%3A07Z&se=2024-09-05T15%3A56%3A07Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-04T22%3A47%3A09Z&ske=2024-09-05T22%3A47%3A09Z&sks=b&skv=2024-08-04&sig=7WvwSmJoDpAHuGiJDO3GhV0MkivLSpbYydIiOwf9ljI%3D", return_base64=False)
    
    # Run the tool to generate the image
    seen_image_text = image2code_tool.run()
    
    # Print the result (either URL or base64 string depending on the return_base64 setting)
    print(f"Interpretation of image: {seen_image_text}")




if __name__ == '__main__':
    #this is for init the agency
    agency.demo_gradio() 
    #test_dalle_image_generator()
    #test_image2code()