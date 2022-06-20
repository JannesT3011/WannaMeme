from config import TOKEN
import discord
from discord import utils
from database.database import DbClient

from cogs.swipe_meme import SwipeMemes

def load_guilds() -> list:
    guilds = [server.id for server in bot.guilds]

    return guilds

bot = discord.Bot(intents=discord.Intents.all())
bot.debug_guilds = load_guilds()
bot.usersdb = DbClient().users_collection
bot.memesdb = DbClient().memes_collection

@bot.event
async def on_ready():
    print(f"{bot.user.id}\n"f"{utils.oauth_url(bot.user.id)}\n"f"{bot.user.name}\n""Ready!")

# COMMANDS
@bot.command(description="Swipe through random memes", aliases=["m"])
async def memes(ctx):
    return await SwipeMemes(bot, ctx).send()

bot.run(TOKEN)