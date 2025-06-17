from fastapi import FastAPI
from app.routes import recommend

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI is running!"}


# Why Register Routers in main.py?
# It keeps your project modular and organized as it grows.
# You can add more routers for different features without cluttering
app.include_router(recommend.router)