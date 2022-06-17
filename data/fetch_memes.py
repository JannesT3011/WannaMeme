import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME
)

subreddit = reddit.subreddit("memes")

def get_meme():
    """GET MEME FROM REDDIT"""

    subreddit = reddit.subreddit("memes")
    meme = subreddit.random()

    return meme.url

def upload_meme_to_db(meme:str):
    """UPLOAD MEME TO DB"""
    return

for _ in range(15):
    meme = get_meme()
    upload_meme_to_db(meme)

print("Done!")