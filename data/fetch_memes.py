import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME
from database.database import Database
import asyncio

db = Database()

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME
)

subreddit = reddit.subreddit("memes")

def get_meme() -> str:
    """GET MEME FROM REDDIT"""

    subreddit = reddit.subreddit("memes")
    meme = subreddit.random()

    return meme.url

async def upload_meme_to_db(meme:str) -> None:
    """UPLOAD MEME TO DB"""
    await db.init_memes_db(meme)
    return

for _ in range(15):
    meme = get_meme()
    asyncio.run(upload_meme_to_db(meme))

print("Done!")