from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker # This import can technically be removed if you only use async_sessionmaker

# postgresql+asyncpg://postgres:yourpassword@localhost/credit_advisor
DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/credit_advisor"

# Create the asynchronous engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True, # Logs SQL queries to the console for debugging
    future=True # Ensures SQLAlchemy 2.0 behavior, though often default now
)

# Use async_sessionmaker to create a factory for AsyncSession objects
# This factory will be an async context manager, handling session creation and closing
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession, # Specify that this factory creates AsyncSession instances
    expire_on_commit=False # Prevents objects from being expired after commit, useful for async
)

# Dependency to get a database session for each request
async def get_db():
    # 'async with' handles session creation and ensures it's closed after the block
    async with AsyncSessionLocal() as session:
        yield session
