from discord.ext import commands
from functions import *

WORLD_CYCLE_DICT = {'duviri':getDuviriCycle,
                    'cetus':getCetusCycle,
                    'earth':getEarthCycle,
                    'cambion':getCambionCycle,
                    'vallis':getVallisCycle,
                    'zariman':getZarimanCycle}

class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def worldstate(self, ctx, arg=''):
        arg = arg.casefold()
        worldState = getWorldState()
        if arg not in WORLD_CYCLE_DICT.keys():
            await ctx.send('World state parameter can be : ' + ', '.join(WORLD_CYCLE_DICT.keys()))
        else:
            await ctx.send(WORLD_CYCLE_DICT[arg](worldState))

    @commands.command()
    async def fissures(self, ctx, *args):
        worldState = getWorldState()
        msg1, msg2 = getFissures(worldState['fissures'], args)
        await ctx.send(msg1)
        await ctx.send(msg2)

    @commands.command()
    async def sortie(self, ctx, v=''):
        worldState = getWorldState()
        msg = getSortie(worldState, True) if v == 'v' else getSortie(worldState)
        await ctx.send(msg)
