from fastapi import APIRouter
from app.schemas.user import UserProfile

router = APIRouter()

@router.post("/recommend")
async def recommend_cards(user: UserProfile):
    # Dummy logic for now
    return {
        "recommended_cards": [
            {"name": "Super Saver Card", "reason": "Best for your spending preferences"}
        ]
    }
