from fastapi import APIRouter, Depends
from app.services.recommend import recommend_cards
from app.schemas.user import UserProfile
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/recommend")
async def get_recommendations(user: UserProfile, db: AsyncSession = Depends(get_db)):
    # Dummy logic for now
    # return {
    #     "recommended_cards": [
    #         {"name": "Super Saver Card", "reason": "Best for your spending preferences"}
    #     ]
    # }
    
    cards = await recommend_cards(user, db)
    return {"recommended_cards": cards}
