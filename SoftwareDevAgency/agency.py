from agency_swarm import Agency
from Devid import Devid
from UIUXDesignerAgent import UIUXDesignerAgent
from RequirementsAnalystAgent import RequirementsAnalystAgent
from CEOAgent import CEOAgent

ceo = CEOAgent()
requirements_analyst = RequirementsAnalystAgent()
uiux_designer = UIUXDesignerAgent()
developer = Devid()

agency = Agency([ceo, [ceo, requirements_analyst],
                 [ceo, uiux_designer],
                 [ceo, developer],
                 [requirements_analyst, uiux_designer],
                 [uiux_designer, developer]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()