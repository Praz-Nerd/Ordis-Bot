from discord.ext import commands
from functions import *

class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def duviri(self, ctx, arg=''):
        worldState = getWorldState()
        if arg.casefold() == 'all':
           await ctx.send(getDuviriCycle(worldState['duviriCycle'], True))
        else:
           await ctx.send(getDuviriCycle(worldState['duviriCycle']))

async def bind(bot):
    await bot.add_cog(API(bot))
