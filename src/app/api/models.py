from typing import List,Any
from pydantic import BaseModel

class Neighbours(BaseModel):
    neighbours: List[str]
    dist: List[float]

class Content(BaseModel):
    skill_name: str
    approach: str