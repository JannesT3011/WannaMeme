import discord

class Help(discord.Embed):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(
            title="WannaMeme - Help",
            description="Swipe through random memes!",
            color=discord.Color.blurple(),
        )
        self.add_field(name="Commands", value="`/meme`: Swipe through random memes!")
        self.set_footer(text=f"{self.bot.version} • made with ❤️ by {self.bot.creator}", icon_url=self.bot.user.display_avatar.url)