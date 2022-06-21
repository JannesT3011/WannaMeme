import discord
from discord.ui import Button, View
import sys
from pymongo import MongoClient
from config import CONNECTION, CLUSTER, MEMESDB
import random


class ButtonsView(View):
    def __init__(self, bot, ctx, memes:list):
        self.bot = bot
        self.ctx = ctx
        self.already_swiped = []
        self.memes = memes
        super().__init__(timeout=None)
    
    #@discord.ui.button(emoji="👍", style=discord.ButtonStyle.green)
    #async def like_button(self, button, interaction):
    #    meme = SwipeMemes(self.bot, self.ctx).load_meme()
#
    #    await interaction.response.edit_message(embed=discord.Embed(title="Meme!").set_image(url=meme))
    #
#
    #
    #@discord.ui.button(emoji="👎", style=discord.ButtonStyle.red)
    #async def disliked_button(self, button, interaction):
    #    meme = SwipeMemes(self.bot, self.ctx).load_meme()
#
    #    await interaction.response.edit_message(embed=discord.Embed(title="Meme!").set_image(url=meme))
    #
    #@discord.ui.button(emoji="⭐", style=discord.ButtonStyle.grey)
    #async def fav_button(self, button, interaction):
    #    meme = SwipeMemes(self.bot, self.ctx).load_meme()
#
    #    await interaction.response.edit_message(embed=discord.Embed(title="Meme!").set_image(url=meme))
    #
    @discord.ui.button(emoji="➡️")
    async def next_button(self, button, interaction):
        meme = SwipeMemes(self.bot, self.ctx).load_meme()
        if len(self.already_swiped) == len(self.memes):
            print(True)
            await interaction.response.edit_message(embed=discord.Embed(title="No more images!"), view=None)
        while meme in self.already_swiped:
            meme = SwipeMemes(self.bot, self.ctx).load_meme()
        self.already_swiped.append(meme)

        await interaction.response.edit_message(embed=discord.Embed(title=meme["name"]).set_image(url=meme["url"]), view=self)

    async def on_timeout(self) -> None:
        for item in self.children:
            self.remove_item(item)

        # Step 3
        #await self.message.edit(view=self) 



class SwipeMemes:
    def __init__(self, bot ,ctx) -> None:
        self.ctx = ctx
        self.bot = bot
        cluster = MongoClient(CONNECTION)
        db = cluster[CLUSTER]
        collection = db[MEMESDB]
        self.memes = [item for item in collection.find({})]
    
    async def add_to_liked(self) -> None:
        return
    
    async def add_to_favs(self) -> None:
        return
    
    async def add_to_already_swiped(self) -> None:
        return
    
    async def load_favs(self, author:str) -> list:
        return


    def load_meme(self) -> dict:
        meme = random.choice(self.memes)

        return {"url": meme["_id"], "name": meme["name"]}
            

    async def send(self) -> discord.Message:
        embed = discord.Embed(title=self.load_meme()["name"]).set_image(url=self.load_meme()["url"])
        return await self.ctx.send(embed=embed, view=ButtonsView(self.bot, self.ctx, self.memes))
