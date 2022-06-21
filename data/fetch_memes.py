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

async def get_meme() -> dict:
    """GET MEME FROM REDDIT"""

    subreddit = await reddit.subreddit("memes")
    meme = await subreddit.random()
    await reddit.close()

    return {"url": meme.url, "name": meme.title} # TODO auch den namen!

async def upload_meme_to_db(meme:str, name:str) -> None:
    """UPLOAD MEME TO DB"""
    await db.init_memes_db(meme, name)
    return

async def start():
    print("Start!")
    for i in range(15):
        print(i)
        try:
            meme = await get_meme()
            await upload_meme_to_db(meme["url"], meme["name"])
        except:
            break

loop = asyncio.get_event_loop()
loop.run_until_complete(start()) # TODO nicht täglich ausführen, sondern einfach wenn der bot startet und der Bot einem Server join! (200 memes! limit https://stackoverflow.com/questions/67101891/discord-py-meme-command-takes-a-lot-of-time)
loop()
print("Done!")