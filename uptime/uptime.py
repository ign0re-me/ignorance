from __main__ import send_cmd_help
from discord.ext import commands
from cogs.utils import checks
from datetime import datetime
from random import choice
import discord
import time
import datetime


class Up:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def up(self, ctx):
        """EMBED UPtIME"""  
        channel = ctx.message.channel
        bot = self.bot.user.name
        
        now = datetime.datetime.now()
        uptime = (now - self.bot.uptime).seconds
        uptime = datetime.timedelta(seconds=uptime)
        days = uptime.days
        hours = int(uptime.seconds/3600)
        minutes = int(uptime.seconds % 3600/60)
        
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(title='Uptime  :  {} days {} hours {} minutes'.format(str(days), str(hours), str(minutes), colour=discord.Colour(value=colour)))
             
        await self.bot.send_message(channel, embed=data)
        
def setup(bot):
    n = Up(bot)
    bot.add_cog(n)
