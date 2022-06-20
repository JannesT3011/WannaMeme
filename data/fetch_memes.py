import asyncpraw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME
from database.database import Database
import asyncio

db = Database()

reddit = asyncpraw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME
)

subreddit = reddit.subreddit("memes")

async def get_meme() -> str:
    """GET MEME FROM REDDIT"""

    subreddit = await reddit.subreddit("memes")
    meme = await subreddit.random()

    return meme.url

async def upload_meme_to_db(meme:str) -> None:
    """UPLOAD MEME TO DB"""
    await db.init_memes_db(meme)
    return

async def start():
    print("Start!")
    for i in range(15):
        print(i)
        try:
            meme = await get_meme()
            await upload_meme_to_db(meme)
        except:
            break

loop = asyncio.get_event_loop()
loop.run_until_complete(start())
loop.stop()
print("Done!")