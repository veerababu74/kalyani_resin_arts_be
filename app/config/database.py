from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

client = None
db = None


async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client.get_default_database()
    print("Connected to MongoDB")


async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("MongoDB connection closed")


def get_database():
    return db
