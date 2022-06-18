import motor.motor_asyncio as motor
from datetime import datetime
from config import CONNECTION, CLUSTER, USERSDB, MEMESDB

class DbClient:
    """CREATES A CONNECTION TO YOUR DATABASE"""
    def __init__(self):
        cluster = motor.AsyncIOMotorClient(CONNECTION)
        db = cluster[CLUSTER]
        self.users_collection = db[USERSDB]
        self.memes_collection = db[MEMESDB]

    def __call__(self, *args, **kwargs):
        return self.collection

class Database(DbClient):
    """EXECUTE DATABASE STUFF"""
    async def init_memes_db(self, memeurl: str):
        """INIT THE MEMES DB"""
        try:
            await self.memes_collection.insert_one(memes_db_layout(memeurl))
            return
        except:
            raise

    async def delete_memes_db(self, memeurl: str):
        """DELETE THE MEMES DB"""
        try:
            await self.memes_collection.delete_one({"_id": memeurl})
            return
        except:
            raise


    async def init_users_db(self, userid: str):
        """INIT THE USERS DB"""
        try:
            await self.users_collection.insert_one(users_db_layout(userid))
            return
        except:
            raise

    async def delete_users_db(self, userid: str):
        """DELETE THE USERS DB"""
        try:
            await self.users_collection.delete_one({"_id": userid})
            return
        except:
            raise

def memes_db_layout(memeurl: str) -> dict:
    """DEFAULT MEMES DB LAYOUT"""
    default_data = {"_id": memeurl,
                    "likes": [],
                    "dislikes": [],
                    "created_at": str(datetime.utcnow()),
                    }

    return default_data

def users_db_layout(userid:str) -> dict:
    """DEFAULT USERS DB LAYOUT"""
    default_data = {
        "_id": userid,
        "liked_memes": [],
        "favourites": [],
        "already_swiped": [],
        "created_at": str(datetime.utcnow()),
    }

    return default_data