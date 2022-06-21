from config import TOKEN, CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME
import discord
from discord import utils
from database.database import DbClient, Database
import asyncpraw
import pymongo

from cogs.swipe_meme import SwipeMemes
from cogs.help import Help
db = Database()

reddit = asyncpraw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME
)

def load_guilds() -> list:
    guilds = [server.id for server in bot.guilds]

    return guilds

async def load_memes():
    subreddit = await reddit.subreddit("memes")
    top = subreddit.top(limit=200)
    async for meme in top: 
        try:
            await db.init_memes_db(meme.url, meme.title)
        except pymongo.errors.DuplicateKeyError:
            continue
    
    await reddit.close()

bot = discord.Bot(intents=discord.Intents.all())
bot.debug_guilds = load_guilds()
bot.usersdb = DbClient().users_collection
bot.memesdb = DbClient().memes_collection
bot.creator = "Bmbus#8446"
bot.version = "v0.1"

@bot.event
async def on_ready():
    await load_memes()
    await bot.change_presence(activity=discord.Game(name="/help"))
    print(f"{bot.user.id}\n"f"{utils.oauth_url(bot.user.id)}\n"f"{bot.user.name}\n""Ready!")

# COMMANDS
@bot.command(description="Swipe through random memes", aliases=["m"])
async def memes(ctx):
    return await SwipeMemes(bot, ctx).send()

@bot.command(description="See all commands")
async def help(ctx):
    embed = Help(bot)
    return await ctx.send(embed=embed)

bot.run(TOKEN)