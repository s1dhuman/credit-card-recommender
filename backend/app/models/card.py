from sqlalchemy import Column, Integer, String, JSON, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CreditCard(Base):
    __tablename__ = "credit_cards"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    annual_fee = Column(Float)
    reward_rates = Column(JSON)  # {"travel": 0.05, "dining": 0.03}
    benefits = Column(JSON)      # ["lounge_access", "travel_insurance"]
    eligibility = Column(JSON)   # {"min_income": 500000}
