from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os
from datetime import datetime

# Define a global variable for the storage path
design_docs_path = "design_documentation.json"

class DesignDocumentationTool(BaseTool):
    """
    This tool helps the UI/UX Designer Agent document the design process and store generated designs for future reference.
    It supports saving design descriptions, images, and any relevant notes or feedback.
    """

    design_id: str = Field(
        ..., description="The unique identifier for the design."
    )
    design_description: str = Field(
        ..., description="A description of the design."
    )
    design_image_url: str = Field(
        ..., description="The URL of the generated design image."
    )
    notes: str = Field(
        None, description="Any relevant notes or feedback regarding the design."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        # Load existing design documentation from storage
        if os.path.exists(design_docs_path):
            with open(design_docs_path, 'r') as file:
                design_docs = json.load(file)
        else:
            design_docs = {}

        # Create a new design documentation entry
        design_doc = {
            "design_id": self.design_id,
            "design_description": self.design_description,
            "design_image_url": self.design_image_url,
            "notes": self.notes,
            "timestamp": datetime.now().isoformat()
        }

        # Add the new documentation entry to the existing documentation
        design_docs[self.design_id] = design_doc

        # Save the updated design documentation back to storage
        with open(design_docs_path, 'w') as file:
            json.dump(design_docs, file, indent=4)

        return f"Design documentation for design ID {self.design_id} has been saved."