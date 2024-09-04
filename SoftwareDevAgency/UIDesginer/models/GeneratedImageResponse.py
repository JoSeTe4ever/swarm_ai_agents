from pydantic import BaseModel
import json 

class GeneratedImageResponse(BaseModel):
    image_url: str
    file_image_location: str



# Define the JSON schema for structured output
response_format ={
    "type": "json_schema",
    "json_schema": {
        "name": "math_reasoning",
        "schema": {
            "type": "object",
            "properties": {
                "steps": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "explanation": {"type": "string"},
                            "output": {"type": "string"}
                        },
                        "required": ["explanation", "output"],
                        "additionalProperties": False
                    }
                },
                "final_answer": {"type": "string"}
            },
            "required": ["steps", "final_answer"],
            "additionalProperties": False
        },
        "strict": True
    }
}
