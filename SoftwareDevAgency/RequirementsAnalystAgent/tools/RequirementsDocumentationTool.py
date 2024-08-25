from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os

# Define a global variable for the storage path
storage_path = "requirements_documents.json"

class RequirementsDocumentationTool(BaseTool):
    """
    This tool allows the Requirements Analyst Agent to document and organize software requirements.
    It supports creating, editing, and storing requirement documents in a structured format.
    The tool also allows for categorization and prioritization of requirements.
    """

    action: str = Field(
        ..., description="The action to perform: 'create', 'edit', or 'view'."
    )
    requirement_id: str = Field(
        None, description="The ID of the requirement to edit or view. Not needed for 'create' action."
    )
    title: str = Field(
        None, description="The title of the requirement. Needed for 'create' and 'edit' actions."
    )
    description: str = Field(
        None, description="The description of the requirement. Needed for 'create' and 'edit' actions."
    )
    category: str = Field(
        None, description="The category of the requirement. Needed for 'create' and 'edit' actions."
    )
    priority: str = Field(
        None, description="The priority of the requirement. Needed for 'create' and 'edit' actions."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        if self.action not in ['create', 'edit', 'view']:
            return "Invalid action. Please specify 'create', 'edit', or 'view'."

        # Load existing requirements from storage
        if os.path.exists(storage_path):
            with open(storage_path, 'r') as file:
                requirements = json.load(file)
        else:
            requirements = {}

        if self.action == 'create':
            if not all([self.title, self.description, self.category, self.priority]):
                return "Missing fields for 'create' action. Please provide title, description, category, and priority."
            
            requirement_id = str(len(requirements) + 1)
            requirements[requirement_id] = {
                "title": self.title,
                "description": self.description,
                "category": self.category,
                "priority": self.priority
            }
            message = f"Requirement '{self.title}' created with ID {requirement_id}."

        elif self.action == 'edit':
            if not self.requirement_id or self.requirement_id not in requirements:
                return "Invalid or missing requirement_id for 'edit' action."
            if not any([self.title, self.description, self.category, self.priority]):
                return "No fields provided to update for 'edit' action."

            if self.title:
                requirements[self.requirement_id]["title"] = self.title
            if self.description:
                requirements[self.requirement_id]["description"] = self.description
            if self.category:
                requirements[self.requirement_id]["category"] = self.category
            if self.priority:
                requirements[self.requirement_id]["priority"] = self.priority
            message = f"Requirement ID {self.requirement_id} updated."

        elif self.action == 'view':
            if not self.requirement_id or self.requirement_id not in requirements:
                return "Invalid or missing requirement_id for 'view' action."
            return json.dumps(requirements[self.requirement_id], indent=4)

        # Save the updated requirements back to storage
        with open(storage_path, 'w') as file:
            json.dump(requirements, file, indent=4)

        return message