import json
import os
from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List

# Define the path to the communication messages JSON file
COMMUNICATION_FILE_PATH = "communication_messages.json"

class CommunicationTool(BaseTool):
    """
    A tool that allows two agents to communicate by reading and writing messages to a shared JSON file.
    Agents can post a message, read the latest message, and retrieve a history of messages.
    """
    sender: str = Field(..., description="The name or ID of the agent sending the message.")
    receiver: str = Field(..., description="The name or ID of the agent receiving the message.")
    message: str = Field(..., description="The message content being sent by the sender.")

    def run(self) -> str:
        """
        The run method writes a message from the sender to the receiver in the communication file.
        It also logs the message with a timestamp and allows the receiver to retrieve it later.
        """
        # Load existing communication data from the JSON file
        messages_data = self._load_messages()

        # Create a new message entry
        new_message = {
            "sender": self.sender,
            "receiver": self.receiver,
            "message": self.message,
        }

        # Append the new message to the messages log
        messages_data.append(new_message)

        # Save the updated messages log back to the JSON file
        self._save_messages(messages_data)

        return f"Message from {self.sender} to {self.receiver}: '{self.message}' has been sent."

    def _load_messages(self) -> List[dict]:
        """
        Load the existing messages from the communication file.
        If the file does not exist, return an empty list.
        """
        if os.path.exists(COMMUNICATION_FILE_PATH):
            with open(COMMUNICATION_FILE_PATH, 'r') as file:
                return json.load(file)
        return []

    def _save_messages(self, messages_data: List[dict]) -> None:
        """
        Save the updated messages log to the communication file.
        """
        with open(COMMUNICATION_FILE_PATH, 'w') as file:
            json.dump(messages_data, file, indent=4)

class MessageHistoryTool(BaseTool):
    """
    A tool for retrieving the message history between two agents.
    """
    agent_name: str = Field(..., description="The name or ID of the agent to retrieve messages for.")

    def run(self) -> List[dict]:
        """
        The run method retrieves all messages sent to the agent from the communication file.
        """
        # Load existing communication data from the JSON file
        messages_data = self._load_messages()

        # Filter messages that are sent to the specified agent
        agent_messages = [msg for msg in messages_data if msg['receiver'] == self.agent_name]

        return agent_messages

    def _load_messages(self) -> List[dict]:
        """
        Load the existing messages from the communication file.
        If the file does not exist, return an empty list.
        """
        if os.path.exists(COMMUNICATION_FILE_PATH):
            with open(COMMUNICATION_FILE_PATH, 'r') as file:
                return json.load(file)
        return []
