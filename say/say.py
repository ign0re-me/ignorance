import discord
from discord.ext import commands
from random import choice
from .utils import checks

class Say:
    """Repeats what you tell it to."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True, no_pm=True)
    async def emsay(self, ctx, *, text):
        """Embed Say."""
        channel = ctx.message.channel
        author = ctx.message.author
        server = ctx.message.server
        avatar = author.avatar_url if author.avatar else author.default_avatar_url
        
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(description="" + text, colour=discord.Colour(value=colour))
        
        data.set_author(name=author.name, icon_url=avatar)
        
        await self.bot.send_message(channel, embed=data)
        
    @commands.command(pass_context=True, no_pm=True)
    async def say(self, ctx, *, text):
        """Bot repeats what you tell it to."""
        channel = ctx.message.channel
        await self.bot.send_message(channel, text)

def setup(bot):
    bot.add_cog(Say(bot))

