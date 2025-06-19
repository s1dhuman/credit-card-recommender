# app/schemas/card.py
from pydantic import BaseModel
from typing import Dict, List

class CardCreate(BaseModel):
    name: str
    annual_fee: float
    reward_rates: Dict[str, float]  # {"travel": 0.05, "dining": 0.03}
    benefits: List[str]             # ["lounge_access", "travel_insurance"]
    eligibility: Dict[str, float]   # {"min_income": 500000}
