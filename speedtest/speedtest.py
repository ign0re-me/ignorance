import discord
from discord.ext import commands
from random import choice
import subprocess
import asyncio

class Speedtest:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(1, 300)
    async def speedtest(self, ctx):
        """EMBED SPEEDTEST"""  
        channel = ctx.message.channel
        message = await self.bot.say(content = 'LOADING.....')
                
        SHARE_ITEM = 'Share results: '
        cmd = 'speedtest-cli --share'.split()
        o = subprocess.check_output(cmd)
        o = o.decode().split('\n')
        sl = discord.utils.find(lambda ss: ss.startswith(SHARE_ITEM), o)
        o.remove(sl)
        o = '\n'.join(x for x in o if x)
        sl = sl[len(SHARE_ITEM):]
        bot = self.bot.user.name
        
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(title='SPEEDTEST RESULT: ', colour=discord.Colour(value=colour))
        avatar = self.bot.user.avatar_url if self.bot.user.avatar else self.bot.user.default_avatar_url
        data.set_author(name='{}'.format(bot), icon_url=avatar)
        data.set_thumbnail(url='http://idroot.net/wp-content/uploads/2014/12/speedtest-logo.jpg', width=50, height=50)
        data.add_field(name='\a\n', value=str(o))
        
        await self.bot.send_message(channel, embed=data)
        await self.bot.delete_message(message)
        
def setup(bot):
    n = Speedtest(bot)
    bot.add_cog(n)
