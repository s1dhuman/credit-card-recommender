from sqlalchemy import select, Float  # Change Integer to Float
from app.models.card import CreditCard  # Add this line


async def recommend_cards(user, db):
    result = await db.execute(
        select(CreditCard)
        .where(
            CreditCard.eligibility.op("->>")("min_income").cast(Float) <= user.income
        )
    )
    return result.scalars().all()
