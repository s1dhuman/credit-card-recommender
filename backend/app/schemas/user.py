# Define a Pydantic Schema for User Input
# Pydantic schemas validate incoming data and provide type hints for your API.

from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    income: float
    spending_preferences: list[str]
