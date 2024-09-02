from pydantic import BaseModel
import json 

class GeneratedImageResponse(BaseModel):
    image_url: str
    file_image_location: str