import discord
from discord.ext import commands
from random import choice
from .utils import checks

class DM:
    """DM a user."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def emdm(self, ctx, user : discord.Member, *, texthere):
        """Embed DM a user."""
        channel = ctx.message.channel
        author = ctx.message.author
        server = ctx.message.server
        avatar = author.avatar_url if author.avatar else author.default_avatar_url
        
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(description="" + texthere, colour=discord.Colour(value=colour))
        
        data.set_author(name=author.name, icon_url=avatar)
        
        await self.bot.say(embed=data)
        await self.bot.send_message(user, embed=data)
        await self.bot.purge_from(channel, limit=1)
        
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def dm(self, ctx, user : discord.Member, *, format_msg):
        """DM a user."""
        channel = ctx.message.channel
        await self.bot.send_message(user, format_msg)
        await self.bot.purge_from(channel, limit=1)
        

def setup(bot):
    bot.add_cog(DM(bot))

