from pydantic import BaseModel

class InterpretedImageResponse(BaseModel):
    html: str
    css: str
    javascript: str