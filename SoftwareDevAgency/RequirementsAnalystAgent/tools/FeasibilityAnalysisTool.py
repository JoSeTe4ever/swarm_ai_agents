from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os

# Define a global variable for the storage path
feasibility_reports_path = "feasibility_reports.json"

class FeasibilityAnalysisTool(BaseTool):
    """
    This tool assists the Requirements Analyst Agent in analyzing the feasibility of the gathered requirements.
    It evaluates the technical, financial, and time feasibility of each requirement and provides a feasibility report.
    """

    requirement_id: str = Field(
        ..., description="The ID of the requirement to analyze."
    )
    technical_feasibility: str = Field(
        ..., description="The technical feasibility of the requirement (e.g., 'High', 'Medium', 'Low')."
    )
    financial_feasibility: str = Field(
        ..., description="The financial feasibility of the requirement (e.g., 'High', 'Medium', 'Low')."
    )
    time_feasibility: str = Field(
        ..., description="The time feasibility of the requirement (e.g., 'High', 'Medium', 'Low')."
    )
    comments: str = Field(
        None, description="Additional comments or notes regarding the feasibility analysis."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        # Load existing feasibility reports from storage
        if os.path.exists(feasibility_reports_path):
            with open(feasibility_reports_path, 'r') as file:
                feasibility_reports = json.load(file)
        else:
            feasibility_reports = {}

        # Create a new feasibility report
        feasibility_report = {
            "requirement_id": self.requirement_id,
            "technical_feasibility": self.technical_feasibility,
            "financial_feasibility": self.financial_feasibility,
            "time_feasibility": self.time_feasibility,
            "comments": self.comments
        }

        # Add the new report to the existing reports
        feasibility_reports[self.requirement_id] = feasibility_report

        # Save the updated feasibility reports back to storage
        with open(feasibility_reports_path, 'w') as file:
            json.dump(feasibility_reports, file, indent=4)

        return f"Feasibility report for requirement ID {self.requirement_id} has been created."