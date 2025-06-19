from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models.card import CreditCard
from app.schemas.card import CardCreate
from app.routes import recommend

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI is running!"}

@app.post("/cards/")
async def create_card(
    card_data: CardCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new credit card entry in the database.
    Handles duplicate card names gracefully.
    """
    try:
        new_card = CreditCard(**card_data.dict())
        db.add(new_card)
        await db.commit()
        await db.refresh(new_card)
        return new_card
    except IntegrityError as e:
        await db.rollback()
        # Check if the error is due to duplicate card name
        if "ix_credit_cards_name" in str(e) or "UNIQUE constraint failed" in str(e):
            raise HTTPException(
                status_code=400,
                detail=f"Card name '{card_data.name}' already exists."
            )
        raise HTTPException(status_code=500, detail="Database error")

# Include recommendation router (for /recommend endpoint)
app.include_router(recommend.router)
