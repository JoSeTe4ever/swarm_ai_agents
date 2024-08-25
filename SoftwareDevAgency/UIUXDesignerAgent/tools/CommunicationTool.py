from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os
from datetime import datetime

# Define global variables for the storage paths
messages_storage_path = "communication_messages.json"
meetings_storage_path = "scheduled_meetings.json"

class CommunicationTool(BaseTool):
    """
    This tool enables the UI/UX Designer Agent to communicate with the CEO, Requirements Analyst, and Developer agents.
    It supports sending and receiving messages, and scheduling meetings or discussions to ensure designs align with project goals.
    """

    action: str = Field(
        ..., description="The action to perform: 'send_message', 'receive_messages', or 'schedule_meeting'."
    )
    recipient: str = Field(
        None, description="The recipient of the message or meeting: 'CEO', 'Requirements Analyst', or 'Developer'. Needed for 'send_message' and 'schedule_meeting' actions."
    )
    message: str = Field(
        None, description="The message content. Needed for 'send_message' action."
    )
    meeting_time: str = Field(
        None, description="The time for the scheduled meeting in 'YYYY-MM-DD HH:MM' format. Needed for 'schedule_meeting' action."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        valid_recipients = ['CEO', 'Requirements Analyst', 'Developer']

        if self.action not in ['send_message', 'receive_messages', 'schedule_meeting']:
            return "Invalid action. Please specify 'send_message', 'receive_messages', or 'schedule_meeting'."

        if self.action == 'send_message':
            if not self.recipient or self.recipient not in valid_recipients:
                return "Invalid or missing recipient for 'send_message' action."
            if not self.message:
                return "Missing message content for 'send_message' action."

            # Load existing messages from storage
            if os.path.exists(messages_storage_path):
                with open(messages_storage_path, 'r') as file:
                    messages = json.load(file)
            else:
                messages = []

            # Add the new message
            new_message = {
                "recipient": self.recipient,
                "message": self.message,
                "timestamp": datetime.now().isoformat()
            }
            messages.append(new_message)

            # Save the updated messages back to storage
            with open(messages_storage_path, 'w') as file:
                json.dump(messages, file, indent=4)

            return f"Message sent to {self.recipient}."

        elif self.action == 'receive_messages':
            # Load existing messages from storage
            if os.path.exists(messages_storage_path):
                with open(messages_storage_path, 'r') as file:
                    messages = json.load(file)
            else:
                messages = []

            # Filter messages for the UI/UX Designer Agent
            received_messages = [msg for msg in messages if msg['recipient'] == 'UI/UX Designer']

            return json.dumps(received_messages, indent=4)

        elif self.action == 'schedule_meeting':
            if not self.recipient or self.recipient not in valid_recipients:
                return "Invalid or missing recipient for 'schedule_meeting' action."
            if not self.meeting_time:
                return "Missing meeting time for 'schedule_meeting' action."

            # Validate the meeting time format
            try:
                meeting_time = datetime.strptime(self.meeting_time, '%Y-%m-%d %H:%M')
            except ValueError:
                return "Invalid meeting time format. Please use 'YYYY-MM-DD HH:MM'."

            # Load existing meetings from storage
            if os.path.exists(meetings_storage_path):
                with open(meetings_storage_path, 'r') as file:
                    meetings = json.load(file)
            else:
                meetings = []

            # Add the new meeting
            new_meeting = {
                "recipient": self.recipient,
                "meeting_time": meeting_time.isoformat(),
                "timestamp": datetime.now().isoformat()
            }
            meetings.append(new_meeting)

            # Save the updated meetings back to storage
            with open(meetings_storage_path, 'w') as file:
                json.dump(meetings, file, indent=4)

            return f"Meeting scheduled with {self.recipient} at {self.meeting_time}."